import unittest
from copy import deepcopy
from visual_evidence import raw_visual_record,visual_text
from workbook_io import display_header

class RawVisualEvidenceTests(unittest.TestCase):
    def test_no_observation_or_confidence_is_removed_or_rewritten(self):
        rows=[dict(frame_id='V001',timestamp_seconds=2.5,observation='Looks downward.',confidence='low'),dict(frame_id='V002',timestamp_seconds=3.5,observation='Looks downward.',confidence='high')]
        original=deepcopy(rows)
        record=dict(visual_evidence=dict(visual_observations=rows),visual_evidence_processed={},visual_postprocessing={})
        result=raw_visual_record(record)
        self.assertEqual(result['visual_evidence']['visual_observations'],original)
        self.assertEqual(rows,original)
        self.assertNotIn('visual_evidence_processed',result)
        self.assertNotIn('visual_postprocessing',result)
        self.assertEqual(visual_text(result['visual_evidence']),'[2.5 s] Looks downward.\n[3.5 s] Looks downward.')
        self.assertEqual(raw_visual_record(result),result)
    def test_capitalizes_headers(self):
        self.assertEqual(display_header('people'),'People')
        self.assertEqual(display_header('FAST_Subjects'),'FAST Subjects')

if __name__=='__main__':unittest.main()
