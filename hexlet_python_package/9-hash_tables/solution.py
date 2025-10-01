def get_hash(key):
    return ord(key) % 5

def get_value(hash_table, key):
  index = get_hash(key)
  result = hash_table[index]
  if result is None:
     return 'not found'
  elif key in result:
     return result[1]
  elif key not in result:
     return 'collision'

hash_table = [
    None,
    ("e", "foo"),
    ("f", "baz"),
    ("g", "bar"),
    None
]
print(get_value(hash_table, 'c'))