def all_unique(coll):
    if not coll:
        return True
    for item in coll:
        if coll.count(item) > 1:
            return False
    return True

result = all_unique("lol")
print(result)