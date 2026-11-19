"""Shared Artifact Tool workbook writer and plain entity-column formatting."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import re

ROOT = Path(__file__).resolve().parent
ENTITY_KEYS = ('people', 'locations', 'organizations', 'dates', 'themes', 'perspective')

def display_header(label):
    if re.sub(r'\s+', '', str(label)).casefold() in {'organization', 'organizations', 'organization/initiatives', 'organizations/initiatives'}:
        return 'Organizations/ Initiatives'
    acronyms={'id':'ID','ids':'IDs','json':'JSON','fast':'FAST','asr':'ASR','ucf':'UCF'}
    label=re.sub(r'([a-z])([A-Z])',r'\1 \2',str(label)).replace('_',' ')
    return ' '.join(acronyms.get(word.lower(),word.capitalize()) for word in label.split())

def entity_columns(facets):
    result = {}
    for key in dict.fromkeys([*ENTITY_KEYS, *facets]):
        value = facets.get(key, '')
        text = '; '.join(str(item) for item in value) if isinstance(value, list) else str(value or '')
        result[key] = text.translate(str.maketrans('', '', '"“”'))
    return result

def literal(value):
    if isinstance(value, str):
        if len(value) > 32767:
            raise ValueError('Cell exceeds Excel text limit; retain full content in a sidecar file.')
        return "'" + value if value.startswith(('=', '+', '-', '@')) else value
    return value

def write_workbook(target, sheets, preview_dir=None):
    """Write data sheets through the managed Artifact Tool runtime."""
    dependencies = Path(os.environ.get('ARTIFACT_DEPENDENCIES', Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies'))
    modules = dependencies/'node/node_modules'
    node = dependencies/'node/bin/node'
    if not (modules/'@oai/artifact-tool').exists() or not node.exists():
        raise RuntimeError('Artifact Tool runtime is missing. Set ARTIFACT_DEPENDENCIES to its managed dependency directory.')
    runtime = ROOT/'outputs/workbook_runtime'
    runtime.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=runtime) as tmp:
        folder = Path(tmp)
        (folder/'node_modules').symlink_to(modules, target_is_directory=True)
        shutil.copy2(ROOT/'workbook_writer.mjs', folder/'workbook_writer.mjs')
        cleaned = [dict(item, rows=[[literal(v) for v in row] for row in item['rows']]) for item in sheets]
        target = Path(target).resolve()
        staging = target.with_suffix('.tmp.xlsx')
        spec = dict(output=str(staging), sheets=cleaned, previewDir=str(Path(preview_dir).resolve()) if preview_dir else None)
        (folder/'input.json').write_text(json.dumps(spec, ensure_ascii=False, allow_nan=False))
        subprocess.run([str(node), str(folder/'workbook_writer.mjs'), str(folder/'input.json')],check=True)
        staging.replace(target)
