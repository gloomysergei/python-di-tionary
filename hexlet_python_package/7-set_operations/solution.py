def diff_keys(old, new):
    result = {
        'kept': set(old) & set(new), 
        'added': set(new) - set(old), 
        'removed': set(old) - set(new)
    }
    return result