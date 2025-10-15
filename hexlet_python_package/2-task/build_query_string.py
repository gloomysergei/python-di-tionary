def build_query_string(dct):
  sorted_dict = dict(sorted(dct.items()))
  lst = []
  for key, value in sorted_dict.items():
    lst.append(f'{key}={value}')
  return '&'.join(lst)

result = build_query_string({'b': 100, 'c': 200, 'a': 65})  # 'a=65&b=100&c=200'
print(result)