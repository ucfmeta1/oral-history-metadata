"""Shared response contract for notebook metadata generation."""

def synthesis_schema(keyword_count):
    string = {'type': 'string'}
    strings = {'type': 'array', 'items': string}
    facets = {'people': strings, 'locations': strings, 'organizations': strings,
              'dates': strings, 'themes': strings, 'perspective': string}
    properties = dict(description=string,
        entities_and_facets=dict(type='object', properties=facets, required=list(facets), additionalProperties=False),
        keywords=dict(type='array', items=string, minItems=keyword_count, maxItems=keyword_count),
        evidence_notes=strings, uncertainty_notes=strings)
    return dict(type='object', properties=properties, required=list(properties), additionalProperties=False)

def validate_keywords(metadata, expected):
    keywords = metadata.get('keywords')
    if not isinstance(keywords, list) or any(not isinstance(k, str) or not k.strip() for k in keywords):
        raise ValueError('GPT keywords must be a list of nonempty strings')
    clean = [k.strip() for k in keywords]
    if len(clean) != expected or len({k.casefold() for k in clean}) != expected:
        raise ValueError(f'GPT returned {len(clean)} keywords; expected exactly {expected} distinct keywords')
    metadata['keywords'] = clean
    return metadata

def retrieval_topics(metadata):
    facets = metadata.get('entities_and_facets', {})
    values = facets.get('themes', []) + facets.get('locations', []) + facets.get('organizations', [])
    if not values:
        values = metadata.get('primary_subjects', []) + metadata.get('secondary_subjects', [])
    return list(dict.fromkeys(str(v).strip() for v in values if str(v).strip()))[:8]

def completion_options(model, output_budget):
    """Translate notebook output limits to the model's Chat Completions API."""
    import re
    if output_budget < 1:
        raise ValueError('Output token budget must be positive')
    if re.match(r'^gpt-[56](?:[.\-]|$)', model):
        # Reasoning shares the completion budget; leave room for the JSON output.
        return dict(max_completion_tokens=max(4096, output_budget), reasoning_effort='low')
    return dict(max_tokens=output_budget, temperature=0)
