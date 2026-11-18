"""Collection-specific cataloging rules from the site review."""
import re

UNIVERSAL_FAST = 'September 11 Terrorist Attacks (2001)'
UNIVERSAL_FAST_ID = 'fst01112794'
UNIVERSAL_FAST_URL = 'https://id.worldcat.org/fast/1112794'

def excluded_fast(heading):
    return bool(re.search(r'september 11 terrorist attacks.*\bin art\b', heading, re.I))

def apply_fast_policy(headings):
    """Add the collection event once; remove the rejected art subdivision."""
    result = [UNIVERSAL_FAST]
    for heading in headings:
        if not excluded_fast(heading) and heading.casefold() not in {x.casefold() for x in result}:
            result.append(heading)
    return result

def clock_label(seconds):
    seconds = max(0, int(seconds))
    return f'{seconds // 60}:{seconds % 60:02d}'
