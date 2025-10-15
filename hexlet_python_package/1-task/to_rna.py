def to_rna(dnk):
  template = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
  dnk_list = list(dnk)
  rna_list = [] 
  for item in dnk_list:
    item_rna = template.get(item)
    rna_list.append(item_rna)
  return ''.join(rna_list)

result = to_rna("C")
print(result)
