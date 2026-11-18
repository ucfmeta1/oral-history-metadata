import ast
import json
from pathlib import Path
import unittest
from notebook_contract import retrieval_topics, synthesis_schema, validate_keywords

class NotebookContractTests(unittest.TestCase):
    def test_schema_follows_configured_count(self):
        for count in (5, 8):
            keywords = synthesis_schema(count)['properties']['keywords']
            self.assertEqual((keywords['minItems'], keywords['maxItems']), (count, count))

    def test_eight_keywords_fail_five_keyword_contract(self):
        with self.assertRaisesRegex(ValueError, 'returned 8.*expected exactly 5'):
            validate_keywords({'keywords': list('abcdefgh')}, 5)

    def test_duplicates_are_rejected(self):
        with self.assertRaises(ValueError):
            validate_keywords({'keywords': ['a','b','c','d',' A ']}, 5)

    def test_new_facets_drive_retrieval(self):
        self.assertEqual(retrieval_topics({'entities_and_facets': {'themes':['Family memory'], 'locations':['Sarasota'], 'organizations':['UCF']}}),
                         ['Family memory','Sarasota','UCF'])

    def test_notebook_prompt_and_synthesis_agree(self):
        nb = json.loads(Path('Test_UCFremembers911_video_FAST_metadata.ipynb').read_text())
        tree = ast.parse(''.join(nb['cells'][14]['source']))
        prompt = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SYNTHESIS_PROMPT' for t in n.targets))
        namespace = {'KEYWORD_COUNT': 5}
        exec(compile(ast.Module(body=[prompt], type_ignores=[]), '<prompt>', 'exec'), namespace)
        self.assertIn('exactly 5 distinct', namespace['SYNTHESIS_PROMPT'])
        function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'synthesize')
        def ask(*args, **kwargs):
            self.assertEqual(kwargs['output_schema']['properties']['keywords']['maxItems'], 5)
            return {'description': 'Example', 'keywords': list('abcde'), 'entities_and_facets': {}}
        namespace.update(ask_json=ask, synthesis_schema=synthesis_schema, validate_keywords=validate_keywords,
                         json=json, clean_description=lambda s:s)
        exec(compile(ast.Module(body=[function], type_ignores=[]), '<synthesize>', 'exec'), namespace)
        result = namespace['synthesize'](Path('video.mp4'), {}, [], {})
        self.assertEqual(len(result['keywords']), 5)


class ModelCompatibilityTests(unittest.TestCase):
    def test_reasoning_models_use_completion_limit_without_temperature(self):
        from notebook_contract import completion_options
        for model in ('gpt-6-luna', 'gpt-6.1-sol', 'gpt-5-mini'):
            options = completion_options(model, 1800)
            self.assertNotIn('max_tokens', options)
            self.assertNotIn('temperature', options)
            self.assertGreaterEqual(options['max_completion_tokens'], 4096)
            self.assertEqual(options['reasoning_effort'], 'low')

    def test_legacy_model_keeps_supported_parameters(self):
        from notebook_contract import completion_options
        self.assertEqual(completion_options('gpt-4o', 1800), {'max_tokens': 1800, 'temperature': 0})

    def test_notebook_helper_sends_compatible_request(self):
        from types import SimpleNamespace
        from notebook_contract import completion_options
        nb = json.loads(Path('Test_UCFremembers911_video_FAST_metadata.ipynb').read_text())
        tree = ast.parse(''.join(nb['cells'][10]['source']))
        function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'ask_json')
        captured = {}
        def create(**kwargs):
            captured.update(kwargs)
            return SimpleNamespace(choices=[SimpleNamespace(finish_reason='stop', message=SimpleNamespace(content='{"ok":true}'))])
        namespace = dict(METADATA_MODEL='gpt-6-luna', json=json, completion_options=completion_options,
                         client=SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create))))
        exec(compile(ast.Module(body=[function],type_ignores=[]), '<ask_json>', 'exec'), namespace)
        self.assertEqual(namespace['ask_json']('system', 'user'), {'ok': True})
        self.assertIn('max_completion_tokens', captured)
        self.assertNotIn('max_tokens', captured)
        self.assertNotIn('temperature', captured)

class ExportFailureTests(unittest.TestCase):
    def test_failed_run_preserves_outputs_and_reports_root_cause(self):
        import tempfile
        import pandas as pd
        nb = json.loads(Path('Test_UCFremembers911_video_FAST_metadata.ipynb').read_text())
        source = ''.join(nb['cells'][16]['source'])
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            previous = output/'UCFremembers911_video_metadata.xlsx'
            previous.write_bytes(b'previous valid workbook')
            def fail(video):
                raise ValueError('underlying test error')
            namespace = dict(OUTPUT_DIR=output, pd=pd, videos=[Path('example.mp4')],
                             DRY_RUN=False, tqdm=lambda values, **kwargs: values, process_video=fail, raw_visual_record=lambda r:r)
            with self.assertRaisesRegex(RuntimeError, 'First failure: underlying test error'):
                exec(compile(source, '<export>', 'exec'), namespace)
            self.assertEqual(previous.read_bytes(), b'previous valid workbook')
            self.assertIn('underlying test error', (output/'last_run_errors.csv').read_text())

if __name__ == '__main__':
    unittest.main()
