"""Consistent display formatting without changing source transcripts or authority terms."""
from copy import deepcopy
from datetime import datetime
import re

VISUAL_LABELS = {'attire_and_symbols': 'Attire & Symbols',
                 'artifacts_and_props': 'Artifacts & Props',
                 'activities_and_emotional_moments': 'Activities, Expressions, and Gaze'}

def written_date(value):
    """Expand ISO day/month dates without inventing missing date precision."""
    def replace(match):
        token = match.group()
        try:
            if len(token) == 10:
                date = datetime.strptime(token, '%Y-%m-%d')
                return f'{date:%B} {date.day}, {date.year}'
            date = datetime.strptime(token, '%Y-%m')
            return f'{date:%B} {date.year}'
        except ValueError:
            return token
    return re.sub(r'\b\d{4}-\d{2}(?:-\d{2})?\b', replace, str(value))

def title_text(text):
    connectors = {'and', 'or', 'of', 'the', 'in', 'on', 'to', 'for', 'with', 'a', 'an'}
    def replace(match):
        word = match.group()
        if word.isupper() or any(c.isupper() for c in word[1:]):
            return word
        if match.start() and word.lower() in connectors:
            return word.lower()
        return word[:1].upper() + word[1:]
    return re.sub(r"[^\W\d_]+(?:[’'][^\W\d_]+)*", replace, str(text))

def sentence_text(text):
    text = str(text).strip()
    return re.sub(r'[^\W\d_]', lambda m: m.group().upper(), text, count=1)

def format_metadata(record):
    result = deepcopy(record)
    facets = result.get('entities_and_facets', {})
    facets['dates'] = [written_date(v) for v in facets.get('dates', [])]
    facets['themes'] = [title_text(v) for v in facets.get('themes', [])]
    for item in result.get('visual_evidence', {}).get('visual_observations', []):
        item['observation'] = sentence_text(item['observation'])
    return result
