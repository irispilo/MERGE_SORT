import pytest
from merge_sort import merge_two_lists

MERGE_TWO_LISTS_TEST_CASES = [
    (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
    (([], []), []),
    (([1, 2, 3], []), [1, 2, 3]),
    (([], [4, 5]), [4, 5]),
    (([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3]),
    (([-3, 0, 2], [-2, 1, 5]), [-3, -2, 0, 1, 2, 5]),
]

@pytest.mark.parametrize("inputs, expected", MERGE_TWO_LISTS_TEST_CASES)
def test_merge_two_lists(inputs, expected):
    left, right = inputs
    assert merge_two_lists(left, right) == expected