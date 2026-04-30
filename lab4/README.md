# Python. Лабораторная работа №3
## Замыкания

## Условия задач

- Замыкание для получение текста ответа на запрос к API, например https://dogapi.dog/api/v2/facts.

- Декоратор, ограничивающий частоту вызовов функций.

## Описание проделанной работы
1. Реализация замыкания для работы с API
Замыкание реализовано функцией create_api_function(url). Она принимает URL-адрес API и возвращает внутреннюю функцию get_data(), которая при каждом вызове обращается к этому API.
2. Реализация декоратора для ограничения частоты вызовов
Декоратор rate_limiter(delay_seconds) реализует механизм throttling (ограничение частоты вызовов).
3. Применение декоратора к замыканию
Сначала создаётся функция с замыканием:
```python
dog_api = create_api_function("https://dogapi.dog/api/v2/facts")
```
Затем эта функция декорируется:
```python
dog_api = rate_limiter(3)(dog_api)
```

## Скриншоты результатов

<img width="1347" height="170" alt="image" src="https://github.com/user-attachments/assets/8d9673b8-4a7e-410b-9ff0-5d90169238e5" />


## Ссылки на используемые материалы

1. [Декораторы Python: пошаговое руководство](https://habr.com/ru/companies/otus/articles/727590/)
2. [Замыкания и декораторы в Python:](https://habr.com/ru/companies/otus/articles/727590/)
3. [dogapi.dog](https://dogapi.dog/api/v2/facts)
