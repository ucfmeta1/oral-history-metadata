"""Public metadata views without internal review diagnostics."""
import json
import re
from visual_evidence import visual_json

DIAGNOSTICS = {'quality', 'rubricevaluation', 'evidencenotes', 'uncertaintynotes',
               'uncertainties', 'confidence', 'reviewrequired', 'issues', 'status',
               'remainingissues', 'revisionattempts', 'lowconfidencevisuals',
               'visuallowconfidence', 'visualpostprocessing'}

def presentation_record(value):
    """Retain content and evidence while hiding diagnostic fields recursively."""
    if isinstance(value, dict):
        return {key: presentation_record(item) for key, item in value.items()
                if re.sub(r'[^a-z]', '', key.lower()) not in DIAGNOSTICS}
    if isinstance(value, list):
        return [presentation_record(item) for item in value]
    return value

def presentation_visual_json(visual):
    visual_json(visual)  # Validate the full internal extraction before displaying it.
    return json.dumps(presentation_record(visual), ensure_ascii=False, indent=2, allow_nan=False)
