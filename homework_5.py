# Задача: дан массив целых чисел (может быть неотсортирован).
# Найди все уникальные тройки (a, b, c) такие что a + b + c = 0.
#
# [-1, 0, 1, 2, -1, -4] → [[-1, -1, 2], [-1, 0, 1]]
# [0, 1, 1] → []
# [0, 0, 0] → [[0, 0, 0]]
import pytest


def find_all_unique_triples(arr: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    arr.sort()
    arr_length = len(arr)
    result: list[list[int]] = []

    for i in range(arr_length - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        if arr[i] > 0:
            break

        left, right = i + 1, arr_length - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

    return result


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([-3, -2, 1], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-1, -1, 0, 0, 1, 1], [[-1, 0, 1]]),
        ([1, 2, -3], [[-3, 1, 2]]),
    ],
)
def test_find_all_unique_triples(arr, expected):
    actual = find_all_unique_triples(arr)
    assert (
        actual == expected
    ), f"{find_all_unique_triples.__name__}: {arr} -> {actual}, expected: {expected}"
