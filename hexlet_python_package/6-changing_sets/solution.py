def toggle(flag, st):
    if flag not in st:
        st.add(flag)
    else:
        st.discard(flag)

def toggled(flag, st):
    new_st = st.copy()
    if flag not in new_st:
        new_st.add(flag)
        return new_st
    else:
        new_st.discard(flag)
        return new_st

a, b, c = "abc"
st = {a, b}
print(toggled(c, st))

'''        
a, b, c = "abc"
st = {a, b}
assert toggled(c, flags) is not flags, "Should return a new set!"
assert flags == {a, b}, "Old set should not be changed!"
assert c in toggled(c, flags)
assert b not in toggled(b, flags)
'''

