from collections import Counter

dict = {'one': ['Sergei', 'Larisa']}
def add_values(key, value):
  if key not in dict:
    dict[key] = []
    dict[key].append(value)
  return dict
print(add_values('two', 'Katerina'))

result = dict.setdefault('three', 'Noteun')
print(result)
print(dict)
