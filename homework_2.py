# Задача: дан массив целых чисел.
# Найди длину наибольшей последовательности идущих подряд чисел
# (числа могут быть в любом порядке в массиве).
# [100, 4, 200, 1, 3, 2] → 4 (последовательность 1, 2, 3, 4)
# [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] → 9 (0, 1, 2, 3, 4, 5, 6, 7, 8)

# Шаг 1
# Дано: список целых чисел
# Вернуть: длину наибольшей последовательности идущих подряд чисел
# Вопросы:
# 1. Могут ли числа быть отрицательными?
# 2. Если все числа в списке будут одинаковые?
# 3. Если в списке будет одно число?
# 4. Может ли список быть пустым?
# 5. Если будут найдены более одной последовательности?
# 6. Сколько выводить ответов, первый найденный или все?

# Шаг 2
# [100, 4, 200, 1, 3, 2] → 4
# [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] → 9


# Шаг 3 (brute force)
def find_length_longest_sequence_bruteforce(nums: list[int]) -> int:
    """
    Big-O: O(n^3)
    """
    result = 0

    for i in range(len(nums)):
        count = 1
        while nums[i] + count in nums:
            count += 1

        result = max(result, count)

    return result


# Шаг 4 (optimized)
def find_length_longest_sequence_optimized(nums: list[int]) -> int:
    """
    Big-O: O(n)
    """
    num_set = set(nums)
    result = 0

    for num in num_set:
        if num - 1 in num_set:
            continue

        length = 1
        while num + length in num_set:
            length += 1

        result = max(result, length)

    return result


if __name__ == "__main__":
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([6], 1),
        ([2, 2, 2], 1),
        ([2, 1, 10, 11], 2),
        ([5, 1, 3], 1),
        ([1, 2, 3], 3),
        ([0, 1, 2, 3], 4),
        ([0, 5, 6, 20, 22, 23, 24], 3),
        ([-3, -2, -1, 0, 5], 4),
        ([1, 2, 3, 10, 11], 3),
    ]

    for arr, expected in test_cases:
        print(f"Test case: {arr}")
        print(
            f"Brute force: {find_length_longest_sequence_bruteforce(arr)}, expected: {expected}"
        )
        print(
            f"Optimized: {find_length_longest_sequence_optimized(arr)}, expected: {expected}"
        )
        print()
