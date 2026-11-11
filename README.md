## Курс Алгоритмы для собеседований: Basic

Ссылка на курс: https://run4me.ru/course/algoritmy-dlya-sobesedovaniy-basic

### Урок Linked List

Ссылка на урок: https://run4me.ru/course/algoritmy-dlya-sobesedovaniy-basic/lesson/linked-list

### Домашнее задание

Задача: напиши функцию remove_duplicates(head) которая удаляет все дублирующиеся узлы из несортированного Linked List (
оставляет первое вхождение каждого значения).

Примеры:

- 1 → 2 → 3 → 2 → 1 → None ⇒ 1 → 2 → 3 → None
- 1 → 1 → 1 → None ⇒ 1 → None

Требования:

1. Используй seen = set() для O(1) проверки
2. Измени список in-place (не создавай новый)
3. Укажи Big-O по времени и памяти

Критерии: работает на обоих примерах + Big-O указана.

### Команда запуска

```bash 
pip install pytest
pytest -v homework_8.py
```
