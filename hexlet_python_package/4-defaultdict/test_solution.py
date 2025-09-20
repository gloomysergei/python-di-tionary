from solution import collect_indexes


def test_collect_indexes():
    assert not collect_indexes([])
    assert collect_indexes([1]) == {1: [0]}
    assert collect_indexes([1, 2]) == {1: [0], 2: [1]}
    assert collect_indexes('lol') == {'l': [0, 2], 'o': [1]}
    assert collect_indexes('coco') == {'c': [0, 2], 'o': [1, 3]}