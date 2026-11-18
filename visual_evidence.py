"""Export raw visual observations without filtering, grouping or summarization."""
from copy import deepcopy

def raw_visual_record(record):
    """Discard obsolete processed views while preserving extraction verbatim."""
    result=dict(record)
    result['visual_evidence']=deepcopy(record.get('visual_evidence_raw',record.get('visual_evidence',{})))
    for key in ('visual_evidence_processed','visual_postprocessing','visual_evidence_raw'):
        result.pop(key,None)
    return result

def visual_text(visual):
    """Format each original observation as one line, with its original timestamp."""
    return '\n'.join(f"[{item.get('timestamp_seconds', '')} s] {item.get('observation', '')}" for item in visual.get('visual_observations',[]))
