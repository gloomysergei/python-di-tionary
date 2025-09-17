def count_all(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters

result = count_all('sergei')
print(result)