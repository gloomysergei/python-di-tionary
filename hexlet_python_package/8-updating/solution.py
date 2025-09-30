def apply_diff(st, dict):
    if st == set() or dict == {}:
        return
    set_add = dict.get('add')
    if set_add == None:
        set_add = set()
    set_remove = dict.get('remove')
    if set_remove == None:
        set_remove = set()
    st.update(set_add)
    st.difference_update(set_remove)
    return st 

st = {'a', 'b', 'c'}
dct = {'add': {'c', 'd'}}
print(apply_diff(st, dct))