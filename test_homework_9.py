import pytest
from homework_9 import BrowserHistory


def make_history(*urls: str) -> BrowserHistory:
    """
    Создает историю браузера
    :param urls: Url страниц
    :return: История браузера
    """
    history = BrowserHistory(urls[0])

    for url in urls[1:]:
        history.visit(url)

    return history


def test_set_current() -> None:
    """
    Проверяет установку текущей страницы
    :return: None
    """
    assert BrowserHistory("google.com").current.val == "google.com"


def test_visit_method() -> None:
    """
    Проверяет, что метод visit работает корректно
    :return: None
    """
    history = make_history("google.com", "youtube.com")

    assert history.current.val == "youtube.com"
    assert history.current.prev.val == "google.com"
    assert history.current.next is None


@pytest.mark.parametrize(
    "start, step, expected",
    [
        ("github.com", 1, "youtube.com"),
        ("github.com", 2, "google.com"),
        ("github.com", 5, "google.com"),
        ("github.com", 0, "github.com"),
        ("google.com", 1, "google.com"),
    ],
)
def test_back_method(start, step, expected) -> None:
    """
    Проверяет, что метод back работает корректно
    :param start: Текущая страница
    :param step: Количество шагов
    :param expected: Ожидаемый результат
    :return: None
    """
    history = make_history("google.com", "youtube.com", "github.com")

    while history.current.val != start:
        history.back(1)

    assert history.back(step) == expected
    assert history.current.val == expected


@pytest.mark.parametrize(
    "step, expected",
    [
        (0, "google.com"),
        (1, "youtube.com"),
        (2, "github.com"),
        (5, "github.com"),
    ],
)
def test_forward_method(step, expected) -> None:
    """
    Проверяет, что метод forward работает корректно
    :param step: Количество шагов
    :param expected: Ожидаемый результат
    :return: None
    """
    history = make_history("google.com", "youtube.com", "github.com")
    history.back(5)

    assert history.forward(step) == expected
    assert history.current.val == expected


def test_visit_truncates_forward_history() -> None:
    """
    Проверяет, что метод visit обрезает историю вперед
    :return: None
    """
    history = make_history("google.com", "youtube.com", "github.com")
    history.back(1)

    history.visit("leetcode.com")

    assert history.current.val == "leetcode.com"
    assert history.back(1) == "youtube.com"
    assert history.back(1) == "google.com"
    assert history.forward(1) == "youtube.com"
    assert history.forward(1) == "leetcode.com"


def test_negative_step_raises() -> None:
    """
    Проверяет, что шаги не могут быть отрицательными
    :return: None
    """
    history = make_history("google.com")

    with pytest.raises(ValueError):
        history.back(-1)
    with pytest.raises(ValueError):
        history.forward(-1)
