def toggle(flag, flag_set):
    if flag in flag_set:
        flag_set.discard(flag)
    else:
        flag_set.add(flag)


def toggled(flag, flag_set):
    new_set = flag_set.copy()
    toggle(flag, new_set)
    return new_set