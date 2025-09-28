## Метод difference_update

Метод `difference_update()` обновляет набор, вызывающий метод с разницей наборов.

### Синтаксис

`a.difference_update(b)`

### Пример

```python
A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
diff = A.difference(B)
result = A.difference_update(B)
print(diff) # {'d', 'a'}
print('A = ', A) # A =  {'d', 'a'}
print('B = ', B) # B =  {'f', 'c', 'g'}
print('result = ', result) # result =  None
```

## Метод intersection_update

метод `intersection_update()` обновляет набор, вызывающий метод с пересечением наборов. Пересечение двух или более наборов ‒ это набор элементов, общих для всех наборов.

### Синтаксис

`A.intersection_update(*other_sets)`

### Параметры

Метод `intersection_update` в Python допускает произвольное количество аргументов (наборов).

> Примечание: \* не является частью синтаксиса. Он используется, чтобы указать, что метод допускает произвольное количество аргументов.

### Возвращаемое значение

Этот метод возвращает `None` (то есть не имеет возвращаемого значения). Он только обновляет набор, вызывая метод intersection_update()

### Пример

```python
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
result = A.intersection_update(B)

print('result =', result) # None
print('A =', A) # {2, 3, 4}
print('B =', B) # {2, 3, 4, 5}
```

### Пример

```python
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}
result = C.intersection_update(B, A)
print('result =', result) # None
print('C =', C) # {4}
print('B =', B) # {2, 3, 4, 5, 6}
print('A =', A) # {1, 2, 3, 4}
```
