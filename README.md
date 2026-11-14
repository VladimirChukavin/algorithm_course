## Курс Алгоритмы для собеседований: Basic

Ссылка на курс: https://run4me.ru/course/algoritmy-dlya-sobesedovaniy-basic

### Урок Doubly Linked List

Ссылка на урок: https://run4me.ru/course/algoritmy-dlya-sobesedovaniy-basic/lesson/doubly-linked-list

### Домашнее задание

Задача: реализуй класс BrowserHistory — историю браузера.

Примеры использования методов класса BrowserHistory:
- browser = BrowserHistory("google.com") # стартовая страница
- browser.visit("youtube.com") # перешли
- browser.visit("github.com") # перешли
- browser.back(1) # → "youtube.com" # назад на 1 шаг
- browser.back(1) # → "google.com" # назад ещё на 1
- browser.forward(1) # → "youtube.com" # вперёд на 1
- browser.visit("leetcode.com") # переход обрезает историю вперёд
- browser.forward(2) # → "leetcode.com" # нельзя идти дальше текущей

Требования:
1. Используй двусвязный список (не deque, не Python list)
2. visit, back, forward — все O(1) или O(k), где k — количество шагов
3. Укажи Big-O каждого метода

### Команда запуска

```bash 
pip install pytest
pytest -v test_homework_9.py
```
