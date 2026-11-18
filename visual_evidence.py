"""Export raw visual observations without filtering, grouping or summarization."""
from copy import deepcopy
import json
import math

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


def visual_json(visual):
    """Serialize the reference workbook schema, without rewriting observations."""
    if not isinstance(visual, dict) or set(visual) != {'visual_observations'}:
        raise ValueError('Visual evidence must contain the visual_observations array.')
    observations = visual['visual_observations']
    if not isinstance(observations, list):
        raise ValueError('visual_observations must be an array.')
    required = {'frame_id', 'category', 'observation', 'confidence', 'timestamp_seconds', 'review_required'}
    categories = {'attire_and_symbols', 'artifacts_and_props', 'activities_and_emotional_moments'}
    for item in observations:
        if not isinstance(item, dict) or set(item) != required:
            raise ValueError('Visual observation fields must match the reference workbook schema.')
        if not isinstance(item['frame_id'], str) or not isinstance(item['observation'], str):
            raise ValueError('Frame ID and observation must be strings.')
        if item['category'] not in categories or item['confidence'] not in {'high', 'medium', 'low'}:
            raise ValueError('Invalid visual category or confidence.')
        timestamp = item['timestamp_seconds']
        if type(timestamp) not in (int, float) or not math.isfinite(timestamp) or timestamp < 0:
            raise ValueError('Visual timestamp must be a finite nonnegative number.')
        if type(item['review_required']) is not bool:
            raise ValueError('Visual review_required must be a JSON boolean.')
    return json.dumps(visual, ensure_ascii=False, indent=2, allow_nan=False)
