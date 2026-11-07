# Задача: дана строка. Сожми её — замени повторяющиеся символы на символ и счётчик.
#
# "aabcccdddd" → "a2b1c3d4"
# "abcd" → "a1b1c1d1"
# "aaaa" → "a4"
# "" → ""


def compress_string(row: str) -> str:
    """
    Time Complexity Big-O: O(n)
    Space Complexity Big-O: O(n)
    """
    if not row:
        return ""

    result: list[str] = []
    symbol = row[0]
    counter = 1

    for char in row[1:]:
        if char == symbol:
            counter += 1
            continue
        result.append(f"{symbol}{counter}")
        symbol = char
        counter = 1

    result.append(f"{symbol}{counter}")

    return "".join(result)


if __name__ == "__main__":
    test_cases = [
        ("aabcccdddd", "a2b1c3d4"),
        ("abcd", "a1b1c1d1"),
        ("aaaa", "a4"),
        ("", ""),
        ("aabaa", "a2b1a2"),
        ("abab", "a1b1a1b1"),
        ("aaabbbaaa", "a3b3a3"),
        ("abba", "a1b2a1"),
        ("a", "a1"),
        (" ", " 1"),
    ]

    for string, expected in test_cases:
        actual = compress_string(string)

        assert (
            actual == expected
        ), f"{compress_string.__name__}: {string} -> {actual}, expected: {expected}"

    print(f"All tests passed.")
