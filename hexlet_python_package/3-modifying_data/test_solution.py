import solution


def test_count_empty():
    assert not solution.count_all([])
    assert not solution.count_all("")


def test_count_all():
    assert len(solution.count_all("cat")) == 3
    assert len(solution.count_all("foo")) == 2
    assert list(solution.count_all("dog").values()) == [1, 1, 1]
    assert solution.count_all("ololo")["o"] == 3
