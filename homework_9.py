class Node:
    """
    Класс узла для двусвязаного списка.
    """

    def __init__(self, val: str) -> None:
        """
        Конструктор узла
        :param val: Значение узла
        """
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"Node({self.val})"


class BrowserHistory:
    """
    Класс истории браузера на базе двусвязаного списка.

    Текущая страница - self.current, back/forward доходят
    до границы и возвращают страницу, на которой находятся.
    """

    def __init__(self, homepage: str) -> None:
        """
        Конструктор класса
        :param homepage: Значение первого узла
        """
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        """
        Переход на новую страниц (добавление нового узла),
        обрезает историю вперед.
        Time Complexity: O(1)
        Space Complexity: O(1)
        :param url: Новая страница
        :return: None
        """
        node = Node(url)
        node.prev = self.current
        self.current.next = node
        self.current = node

    def back(self, step: int) -> str:
        """
        Переход назад на количество шагов step.
        Time Complexity: O(1) или O(k), где k — количество шагов
        Space Complexity: O(1)
        :param step: Количество шагов
        :return: Url страницы
        """
        if step < 0:
            raise ValueError("Шаг не может быть отрицательным")

        node = self.current
        for _ in range(step):
            if node.prev is None:
                break
            node = node.prev

        self.current = node

        return node.val

    def forward(self, step: int) -> str:
        """
        Переход вперед на количество шагов step.
        Time Complexity: O(1) или O(k), где k — количество шагов
        Space Complexity: O(1)
        :param step: Количество шагов
        :return: Url страницы
        """
        if step < 0:
            raise ValueError("Шаг не может быть отрицательным")

        node = self.current
        for _ in range(step):
            if node.next is None:
                break
            node = node.next

        self.current = node

        return node.val


if __name__ == "__main__":
    browser = BrowserHistory("google.com")
    browser.visit("youtube.com")
    browser.visit("github.com")
    print(browser.back(1))
    print(browser.back(1))
    print(browser.forward(1))
    browser.visit("leetcode.com")
    print(browser.forward(2))
