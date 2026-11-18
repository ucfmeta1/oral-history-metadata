import json
from pathlib import Path
import tempfile
import unittest
from metadata_policy import UNIVERSAL_FAST, apply_fast_policy
from robust_metadata import Authority, spans, validate_support

class RobustMetadataTests(unittest.TestCase):
    def test_spans_reconstruct_source_without_truncation(self):
        text=('An exact transcript sentence. '*300)+'[PII]'
        chunks=spans(text,200)
        self.assertEqual(''.join(c['text'] for c in chunks),text)
        self.assertTrue(all(c['text']==text[c['start_char']:c['end_char']] for c in chunks))

    def test_invented_or_tiny_quotes_are_rejected(self):
        sources={'T001':'The speaker watched television at work.'}
        for quote in ('invented evidence','The'):
            with self.assertRaises(ValueError):validate_support([{'support':[dict(source_id='T001',quote=quote)]}],sources)
        validate_support([{'support':[dict(source_id='T001',quote='watched television at work')]}],sources)

    def test_policy_is_idempotent_and_excludes_art(self):
        terms=apply_fast_policy(['September 11 Terrorist Attacks (2001) in art','Memory',UNIVERSAL_FAST])
        self.assertEqual(terms,[UNIVERSAL_FAST,'Memory'])
        self.assertEqual(apply_fast_policy(terms),terms)

    def test_hybrid_authority_rejects_deleted_and_unknown_headings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'Topical').mkdir();(root/'Geo').mkdir()
            records=[dict(id='fst00000001',fast='Family memory',deleted=False),dict(id='fst00000002',fast='Deleted heading',deleted=True)]
            (root/'Topical/records.jsonl').write_text('\n'.join(json.dumps(r) for r in records))
            index=Authority(root,root/'cache')
            try:
                self.assertIsNone(index.lookup({'heading':'Invented heading'}))
                self.assertIsNone(index.lookup({'heading':'Deleted heading'}))
                self.assertEqual(index.lexical('Family memory')[0]['id'],'fst00000001')
                metadata=dict(description='A family shares memory',entities_and_facets=dict(themes=['Family memory'],locations=[],organizations=[]))
                found=index.hybrid(metadata,[dict(heading='Family memory'),dict(heading='Invented heading')],None)
                self.assertEqual(len(found),1)
                self.assertEqual(set(found[0]['retrieval_routes']),{'semantic','lexical'})
            finally:index.close()


class FrameSamplingTests(unittest.TestCase):
    def test_adaptive_frames_have_unique_real_timestamps_and_higher_resolution(self):
        import cv2
        import numpy as np
        from robust_metadata import sample_frames
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'test.mp4'
            writer=cv2.VideoWriter(str(path),cv2.VideoWriter_fourcc(*'mp4v'),12,(160,120))
            self.assertTrue(writer.isOpened())
            for i in range(144):
                frame=np.full((120,160,3),40+(i%100),dtype=np.uint8)
                if i>70:cv2.rectangle(frame,(25,20),(100,90),(220,30,200),-1)
                writer.write(frame)
            writer.release()
            frames,duration=sample_frames(path,24)
            self.assertEqual(len(frames),24)
            self.assertEqual(len({f['timestamp_seconds'] for f in frames}),24)
            self.assertTrue(all(0<=f['timestamp_seconds']<duration for f in frames))
            self.assertTrue(all(f['data_url'].startswith('data:image/jpeg;base64,') for f in frames))
            self.assertEqual(sum(f['selection']=='coverage' for f in frames),12)
            reduced,duration=sample_frames(path)
            self.assertEqual(len(reduced),8)
            self.assertEqual(len({f['timestamp_seconds'] for f in reduced}),8)
            self.assertEqual(sum(f['selection']=='coverage' for f in reduced),6)
            self.assertTrue(all(0<=f['timestamp_seconds']<duration for f in reduced))

class SourceBindingTests(unittest.TestCase):
    def test_passages_are_copied_from_source_not_generated_by_model(self):
        from robust_metadata import bind_support
        source={'T001':'A source passage with exact punctuation, [PII], and line breaks.\nNext line.'}
        items=[dict(support=[dict(source_id='T001')])]
        bind_support(items,source)
        self.assertEqual(items[0]['support'][0]['quote'],source['T001'])
        with self.assertRaises(ValueError):bind_support([dict(support=[dict(source_id='invented')])],source)

if __name__ == '__main__':
    unittest.main()
