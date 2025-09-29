def apply_diff(st, dict):
    set_add = dict.get('add')
    print(set_add)
    set_remove = dict.get('remove')
    print(set_remove)
    st.union(set_add)
    st.difference(set_remove)
    return st 

st = {'a', 'b', 'c'}
dct = {'add': {'c', 'd'}}
print(apply_diff(st, dct))