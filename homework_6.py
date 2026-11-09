# Задача: дана строка s содержащая только строчные латинские буквы.
# Найди длину наидлиннейшей подстроки в которой можно заменить
# не более k символов, чтобы все символы стали одинаковыми.
#
# s = "AABABBA", k = 1 → 4 ("AABA" → заменить B → "AAAA")
# s = "ABAB", k = 2 → 4 ("ABAB" → заменить два A → "BBBB")
import pytest


def find_length_longest_substring(string: str, k: int) -> int:
    """
    Находит длину наидлиннейшей подстроки в которой можно заменить
    не более k символов чтобы все символы стали одинаковыми.

    Time Complexity: O(n)
    Space Complexity: O(1), так как алфавит фиксирован
    (строчные латинские буквы)

    :param string: Исходная строка
    :param k: Максимальное количество замен
    :return: Длина наидлиннейшей подстроки
    """
    char_freq: dict[str, int] = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(string):
        char_freq[ch] = char_freq.get(ch, 0) + 1

        while (right - left + 1) - max(char_freq.values()) > k:
            char_freq[string[left]] -= 1

            if char_freq[string[left]] == 0:
                del char_freq[string[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


@pytest.mark.parametrize(
    "string, k, expected",
    [
        ("AABABBA", 1, 4),
        ("ABAB", 2, 4),
        ("", 1, 0),
        ("A", 0, 1),
        ("AB", 0, 1),
        ("AAA", 0, 3),
        ("AAB", 1, 3),
        ("ABCD", 10, 4),
        ("AABBBCCCC", 2, 6),
    ],
)
def test_find_length_longest_substring(string, k, expected):
    actual = find_length_longest_substring(string, k)
    assert actual == expected
