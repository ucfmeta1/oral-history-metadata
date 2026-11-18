import unittest
import json
from copy import deepcopy
from visual_evidence import raw_visual_record,visual_text,visual_json
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
    def test_reference_json_schema_round_trip(self):
        item=dict(frame_id='V001',category='attire_and_symbols',observation='Wears glasses.',confidence='high',timestamp_seconds=2.0,review_required=False)
        visual=dict(visual_observations=[item])
        encoded=visual_json(visual)
        self.assertEqual(json.loads(encoded),visual)
        self.assertIn('\n',encoded)
        for invalid in ({'visual_observations':'summary'}, {'summary':'text'}, {'visual_observations':[dict(item,review_required='false')]}, {'visual_observations':[dict(item,timestamp_seconds=float('nan'))]}):
            with self.assertRaises(ValueError):visual_json(invalid)

    def test_capitalizes_headers(self):
        self.assertEqual(display_header('people'),'People')
        self.assertEqual(display_header('FAST_Subjects'),'FAST Subjects')

if __name__=='__main__':unittest.main()
