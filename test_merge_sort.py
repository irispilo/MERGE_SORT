import pytest
from merge_sort import merge_sort

MERGE_SORT_TEST_CASES = [
    ([3, 1, 4, 1, 5, 9, 2], [1, 1, 2, 3, 4, 5, 9]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([], []),
    ([42], [42]),
    ([-5, 0, -3, 8], [-5, -3, 0, 8]),
    ([7, 7, 7, 7], [7, 7, 7, 7]),
]

@pytest.mark.parametrize("input_list, expected", MERGE_SORT_TEST_CASES)
def test_merge_sort(input_list, expected):
    assert merge_sort(input_list.copy()) == expected