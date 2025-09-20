def collect_indexes(coll):
  dict = {}
  for index in range(len(coll)):
    item = coll[index]
    dict.setdefault(item, []).append(index)
  return dict

result = collect_indexes('cool')
print(result)