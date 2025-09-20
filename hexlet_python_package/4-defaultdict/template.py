from collections import defaultdict

d = defaultdict(int)
d['a'] += 5
d['b'] = d['c'] + 10
print(d) # {'a': 5, 'c': 0, 'b': 10}

def new_value():
  return 'foo'

x = defaultdict(new_value)
x[1]
x['bar']
print(x) # {1: 'foo', 'bar': 'foo'}

# Определение количества вхождений символов в строке
my_dict = defaultdict(int)
for letter in 'Hello, Sergei':
  my_dict[letter] += 1
print(my_dict) 
# {'H': 1, 'e': 3, 'l': 2, 'o': 1, ',': 1, ' ': 1, 'S': 1, 'r': 1, 'g': 1, 'i': 1}