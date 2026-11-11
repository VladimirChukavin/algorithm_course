import pytest


class Node:
    """
    Класс узла для связанного списка
    """

    def __init__(self, val):
        """
        Конструктор узла
        :param val: Значение узла
        """
        self.val = val
        self.next = None


def build_linked_list(values: list[int]) -> Node:
    """
    Создает связанный список из узлов
    :param values: Список значений
    :return: Связанный список
    """
    head = Node(0)
    tail = head

    for val in values:
        tail.next = Node(val)
        tail = tail.next

    return head.next


def to_list(head: Node | None) -> list:
    """
    Трансформирует связанный список в список значений
    :param head: Связанный список
    :return: Список значений
    """
    current = head
    result = []

    while current:
        result.append(current.val)
        current = current.next

    return result


def remove_duplicates(head: Node | None) -> Node | None:
    """
    Удаляет все дублирующиеся узлы из несортированного Linked List
    (оставляет первое вхождение каждого значения).
    Список изменяется на месте.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param head: Исходный список
    :return: Список без дублей
    """
    if head is None:
        return None

    seen = {head.val}
    current = head

    while current.next:
        if current.next.val in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next

    return head


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 2, 1], [1, 2, 3]),
        ([1, 1, 1], [1]),
        ([], []),
        ([7], [7]),
        ([1, 1], [1]),
        ([2, 3, 3], [2, 3]),
        ([1, 2, 1, 2, 1], [1, 2]),
    ],
)
def test_remove_duplicates(values: list[int], expected: list[int]) -> None:
    """
    Тесты для функции remove_duplicates
    :param values: Тестовые данные
    :param expected: Ожидаемые результаты
    :return: None
    """
    head = build_linked_list(values)
    actual = remove_duplicates(head)
    result = to_list(actual)
    assert head is actual, f"{head} is not {actual}"
    assert result == expected, f"{result} != {expected}"
