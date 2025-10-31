from collections import Counter


def scrabble(symbol_set, world):
    dict_symbol = Counter(symbol_set.lower())
    dict_world = Counter(world.lower())
    for key_world, num_world in dict_world.items():
        if key_world not in dict_symbol:
            return False
        elif dict_symbol.get(key_world) < num_world:
            return False
    return True



result = scrabble('scriptingjava', 'JavaScript')
print(result)