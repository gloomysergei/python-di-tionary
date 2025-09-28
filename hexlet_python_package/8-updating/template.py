A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'} 
diff = A.difference(B)
result = A.difference_update(B)
print(diff)
print('A = ', A) 
print('B = ', B) 
print('result = ', result)