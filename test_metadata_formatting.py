from copy import deepcopy
import unittest
from metadata_formatting import written_date, title_text, format_metadata

class FormattingTests(unittest.TestCase):
    def test_written_dates_preserve_precision_and_annotations(self):
        self.assertEqual(written_date('2026-09-11 (recorded)'), 'September 11, 2026 (recorded)')
        self.assertEqual(written_date('2001-09'), 'September 2001')
        self.assertEqual(written_date('September 11, 2001'), 'September 11, 2001')
        self.assertEqual(written_date('2001'), '2001')
        self.assertEqual(written_date('2026-02-31'), '2026-02-31')

    def test_capitalization_preserves_acronyms_and_original_source(self):
        self.assertEqual(title_text('television coverage and UCF memories'), 'Television Coverage and UCF Memories')
        source=dict(entities_and_facets=dict(dates=['2026-09-11'],themes=['family memory']),
                    visual_evidence=dict(visual_observations=[dict(observation='wears a UCF shirt.')]))
        original=deepcopy(source);formatted=format_metadata(source)
        self.assertEqual(source,original)
        self.assertEqual(formatted['entities_and_facets']['themes'],['Family Memory'])
        self.assertEqual(formatted['visual_evidence']['visual_observations'][0]['observation'],'Wears a UCF shirt.')

if __name__=='__main__':unittest.main()
