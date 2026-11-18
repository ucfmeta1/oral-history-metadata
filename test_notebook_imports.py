"""Check that saved notebook imports refer to real helper exports."""
import ast
import importlib
import json
from pathlib import Path
import unittest

class NotebookImportTests(unittest.TestCase):
    def test_all_local_notebook_imports_resolve(self):
        notebook=json.loads(Path('Test_UCFremembers911_video_FAST_metadata.ipynb').read_text())
        checked=[]
        for i,cell in enumerate(notebook['cells']):
            if cell['cell_type']!='code':continue
            tree=ast.parse(''.join(cell['source']))
            for statement in ast.walk(tree):
                if not isinstance(statement,ast.ImportFrom) or not statement.module:continue
                if not Path(statement.module+'.py').exists():continue
                module=importlib.import_module(statement.module)
                for name in statement.names:
                    self.assertTrue(hasattr(module,name.name),f'Cell {i}: {statement.module} does not export {name.name}')
                    checked.append((statement.module,name.name))
        self.assertIn(('workbook_io','display_header'),checked)

if __name__=='__main__':unittest.main()
