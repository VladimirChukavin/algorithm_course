# Задача: дан массив целых чисел. Удали все дубликаты и верни
# массив с уникальными элементами в том же порядке, что и оригинал.
#
# [1, 3, 1, 2, 3, 4] → [1, 3, 2, 4]
# [5, 5, 5] → [5]
# [] → []


def get_array_unique_elements_bruteforce(arr: list[int]) -> list[int]:
    """
    Big-O: O(n^2)
    """
    result: list[int] = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and arr[i] not in result:
                result.append(arr[i])

    return result


def get_array_unique_elements_optimized(arr: list[int]) -> list[int]:
    """
    Big-O: O(n)
    """
    seen: set[int] = set()
    result: list[int] = []

    for element in arr:
        if element in seen:
            continue
        seen.add(element)
        result.append(element)

    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 1, 2, 3, 4], [1, 3, 2, 4]),
        ([5, 5, 5], [5]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, -1, 0, -1], [0, -1]),
    ]

    for arr, expected in test_cases:
        actual_bruteforce = get_array_unique_elements_bruteforce(arr)
        actual_optimized = get_array_unique_elements_optimized(arr)

        assert (
            actual_bruteforce == expected
        ), f"{get_array_unique_elements_bruteforce.__name__}: {arr} -> {actual_bruteforce}, expected: {expected}"
        assert (
            actual_optimized == expected
        ), f"{get_array_unique_elements_optimized.__name__}: {arr} -> {actual_optimized}, expected: {expected}"

        print(f"All tests for case {arr} passed.")
