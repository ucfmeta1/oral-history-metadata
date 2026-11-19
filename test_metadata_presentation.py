"""Ensure README exports omit internal diagnostics without changing content."""
from copy import deepcopy
import json
import unittest
from examples.build_readme_example import build
from metadata_presentation import presentation_record, presentation_visual_json

class PresentationTests(unittest.TestCase):
    def test_nested_diagnostics_are_hidden_without_modifying_source(self):
        source={'description':'An interview.', 'quality':{'status':'needs_review','issues':['Check']},
                'uncertainty_notes':['Unknown'], 'visual_evidence':{'visual_observations':[
                    dict(frame_id='V001',category='attire_and_symbols',observation='Wears glasses.',
                         timestamp_seconds=2.0,confidence='high',review_required=False)]}}
        before=deepcopy(source);clean=presentation_record(source)
        self.assertEqual(source,before)
        self.assertNotIn('quality',clean)
        self.assertNotIn('uncertainty_notes',clean)
        observation=clean['visual_evidence']['visual_observations'][0]
        self.assertEqual(set(observation),{'frame_id','category','observation','timestamp_seconds'})
        self.assertEqual(json.loads(presentation_visual_json(source['visual_evidence'])),clean['visual_evidence'])

    def test_readme_labels_and_visual_json_hide_diagnostics(self):
        record=dict(video_filename='Lundy-Ken-2026-09-11_Video.mp4',speaker_name='Ken Lundy',
            duration_seconds=187,sampled_frames=8,description='Ken Lundy recalls the events.',
            entities_and_facets=dict(people=['Ken Lundy']),keywords=['Memory'],fast_subjects=['Memory'],
            fast_candidates=[dict(heading='Memory',id='fst00000001')],
            quality=dict(status='needs_review',issues=['Internal note']),uncertainty_notes=['Internal note'],
            visual_evidence=dict(visual_observations=[dict(frame_id='V001',category='attire_and_symbols',
                observation='Wears glasses.',confidence='high',timestamp_seconds=2,review_required=False)]))
        panel=build(record)
        self.assertNotIn('<strong>Artifacts and props</strong>',panel)
        self.assertIn('[2 s] Wears glasses.',panel)
        self.assertNotIn('<h4>Visual evidence</h4>',panel)
        self.assertIn('"timestamp_seconds": 2',panel)
        empty=deepcopy(record)
        empty['visual_evidence']['visual_observations']=[]
        self.assertNotIn('visual evidence',build(empty).lower())
        activities=deepcopy(record)
        activities['visual_evidence']['visual_observations'][0].update(
            category='activities_and_emotional_moments',observation='At 8 s, Looks downward.',timestamp_seconds=8)
        self.assertIn('Looks downward.',build(activities))
        self.assertNotIn('At 8 s,',build(activities))
        self.assertIn('[8 s] Looks downward.',build(activities))
        self.assertIn('"timestamp_seconds": 8',build(activities))
        with_artifact=deepcopy(record)
        with_artifact['visual_evidence']['visual_observations'].append(dict(frame_id='V002',category='artifacts_and_props',
            observation='Holds a photograph.',confidence='high',timestamp_seconds=4,review_required=False))
        self.assertIn('<strong>Artifacts and props</strong>',build(with_artifact))
        self.assertIn('Holds a photograph.',build(with_artifact))
        self.assertIn('4 s · V002',build(with_artifact))
        for label in ('<h4>Description</h4>','<h4>FAST Subjects</h4>'):
            self.assertIn(label,panel)
        for label in ('Generated description','Selected FAST subjects','Review status','Review issues','Uncertainties',
                      'confidence:', 'review required:', '"confidence"','"review_required"'):
            self.assertNotIn(label,panel)

if __name__=='__main__':unittest.main()
