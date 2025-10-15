def build_query_string(params):
    items = []
    for key, value in sorted(params.items()):
        items.append(f'{key}={value}')
    return '&'.join(items)