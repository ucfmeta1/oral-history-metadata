"""Execute the supplied notebook in this project's virtual environment."""
import json
import os
from pathlib import Path
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent
out = root / 'outputs/notebook'
out.mkdir(parents=True, exist_ok=True)
# Keep model downloads, Jupyter files and Python caches within the workspace.
for variable, path in {'HF_HOME': out/'model_cache', 'XDG_CACHE_HOME': out/'system_cache',
                       'IPYTHONDIR': out/'ipython', 'JUPYTER_RUNTIME_DIR': out/'runtime',
                       'PYTHONPYCACHEPREFIX': out/'pycache'}.items():
    os.environ.setdefault(variable, str(path))
kernels = out / 'jupyter/kernels/library-project'
kernels.mkdir(parents=True, exist_ok=True)
(kernels/'kernel.json').write_text(json.dumps(dict(argv=[str(root/'.venv/bin/python'), '-m', 'ipykernel_launcher', '-f', '{connection_file}'], display_name='Library Project', language='python')))
os.environ['JUPYTER_PATH'] = str(out/'jupyter') + os.pathsep + os.environ.get('JUPYTER_PATH', '')
notebook = nbformat.read(root/'Test_UCFremembers911_video_FAST_metadata.ipynb', as_version=4)
class StreamingNotebookClient(NotebookClient):
    def process_message(self, msg, cell, cell_index):
        if msg.get('msg_type') == 'stream':
            print(msg.get('content', {}).get('text', ''), end='', flush=True)
        return super().process_message(msg, cell, cell_index)

client = StreamingNotebookClient(notebook, timeout=1800, kernel_name='library-project', resources={'metadata': {'path': str(root)}})
async def progress(cell, cell_index, **kwargs):
    if cell.cell_type == 'code':
        print(f'Executing cell {cell_index}...', flush=True)
client.on_cell_start = progress
try:
    client.execute()
finally:
    target = out/'Test_UCFremembers911_video_FAST_metadata.executed.ipynb'
    nbformat.write(notebook, target)
    print(f'Executed notebook saved: {target}', flush=True)
