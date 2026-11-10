# Задача: дан массив целых чисел (положительных и отрицательных).
# Найди длину наибольшего подмассива с суммой равной нулю.
#
# [15, -2, 2, -8, 1, 7, 10, 23] → 5 (подмассив [-2, 2, -8, 1, 7])
# [1, 2, 3] → 0 (нет подмассива с суммой 0)
# [0, 0, 0] → 3

import pytest


def find_length_largest_subarray(arr: list[int]) -> int:
    """
    Находит длину наибольшего подмассива с суммой равной нулю.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param arr: Исходный массив
    :return: Длина наибольшего подмассива
    """
    prefix_index: dict[int, int] = {0: -1}
    total = 0
    max_len = 0

    for i, num in enumerate(arr):
        total += num

        if total in prefix_index:
            max_len = max(max_len, i - prefix_index[total])
        else:
            prefix_index[total] = i

    return max_len


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([15, -2, 2, -8, 1, 7, 10, 23], 5),
        ([1, 2, 3], 0),
        ([0, 0, 0], 3),
        ([], 0),
        ([0], 1),
        ([1], 0),
        ([1, -1], 2),
        ([1, -1, 1, -1], 4),
        ([5, 5, -10], 3),
        ([3, -1, -2], 3),
    ],
)
def test_find_length_largest_subarray(arr, expected):
    actual = find_length_largest_subarray(arr)
    assert actual == expected, f"{arr} -> {actual} != {expected}"
