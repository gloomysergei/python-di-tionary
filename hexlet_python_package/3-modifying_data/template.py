def template(coll):
  dist ={}
  for item in coll:
    count = 0
    for elem in coll:
      if item == elem:
        count += 1
    dist[item] = count
  return dist

## coll = [10, 11, 10, 11, 13, 20]
## print(template(coll))
    
    
