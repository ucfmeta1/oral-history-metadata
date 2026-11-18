"""Offline regression tests for the notebook's report-evidence worksheets."""
import ast
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import pandas as pd
from openpyxl import load_workbook
from metadata_policy import UNIVERSAL_FAST
from workbook_io import write_workbook, display_header

class EvidenceExportTests(unittest.TestCase):
    def test_evidence_and_review_flags_round_trip_without_api_calls(self):
        notebook=json.loads(Path('Test_UCFremembers911_video_FAST_metadata.ipynb').read_text())
        tree=ast.parse(''.join(notebook['cells'][8]['source']))
        function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='evidence_sheets')
        ns=dict(pd=pd,UNIVERSAL_FAST=UNIVERSAL_FAST,display_header=display_header)
        exec(compile(ast.Module(body=[function],type_ignores=[]),'<evidence_export>','exec'),ns)
        support=dict(source_id='T001',quote='An exact original passage.')
        record=dict(video_filename='example.mp4',quality=dict(status='needs_review',issues=['Check ambiguous person'],attempts=2,visual_low_confidence=1,specific_fast_count=1),
            fast_subjects=[UNIVERSAL_FAST,'Memory'],source_spans=[dict(id='T001',text=support['quote'],start_char=0,end_char=26)],
            source_context='Recording metadata',collection_context='Collection event',
            description_support=[dict(text='A supported sentence.',support=[support])],
            keyword_support=[dict(term='Family memory',support=[support])],
            fast_selection_details=[dict(heading=UNIVERSAL_FAST,authority_id='fst01112794',reason='Collection policy'),
                                    dict(heading='Memory',authority_id='fst00000001',rationale='Central topic',support=[support])],
            visual_evidence=dict(visual_observations=[dict(frame_id='V001',timestamp_seconds=2.5,category='artifacts_and_props',
                observation='=example formula-like source text',confidence='low',review_required=True)]))
        with TemporaryDirectory() as tmp:
            target=Path(tmp)/'evidence.xlsx'
            sheets, summary=ns['evidence_sheets']([record])
            write_workbook(target,sheets)
            self.assertEqual(summary.iloc[0]['Status'],'needs_review')
            workbook=load_workbook(target,data_only=True)
            self.assertEqual(len(workbook.sheetnames),6)
            self.assertEqual(workbook['Description_Evidence']['E2'].value,support['quote'])
            self.assertEqual(workbook['Keyword_Evidence']['C2'].value,'T001')
            self.assertEqual(workbook['FAST_Selection']['D2'].value,'Collection policy')
            self.assertEqual(workbook['Visual_Evidence']['G2'].value,True)
            self.assertEqual(workbook['Visual_Evidence']['E2'].data_type, 's')
            self.assertEqual(workbook['Visual_Evidence']['E2'].value.lstrip("'"), '=example formula-like source text')
            self.assertEqual(workbook['Quality_Review']['C2'].value,'Check ambiguous person')
            self.assertEqual(workbook['Evidence_Sources'].max_row,4)
            workbook.close()

if __name__=='__main__':unittest.main()
