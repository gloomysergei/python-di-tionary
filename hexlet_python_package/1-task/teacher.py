MAPPING = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}
def to_rna(dna):
    rna = []
    for nucliotide in dna:
        rna.append(MAPPING[nucliotide])
    return ''.join(rna)

# Альтернативный вариант с использованием map
# def to_rna(dna):
#     return ''.join(map(MAPPING.get, dna))
# END