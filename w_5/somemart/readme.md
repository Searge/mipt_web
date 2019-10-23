# Описание задания

В этом задании вам требуется реализовать часть API интернет-магазина. В частности, этот API должен позволять создавать товары и отзывы к этим товарам.

Вы можете считать, что вам очень повезло с заказчиком, так как точки API, которые необходимо реализовать, строго ограничены по формату:

`(POST) /api/v1/goods/` - создать товар в магазине
Формат запроса: `application/json`
Пример запроса:

```python
{
"title": "Сыр \"Российский\"",
"description": "Очень вкусный сыр, да еще и российский.",
"price": 100
}
```

Ограничения:

- Все поля обязательные
- title - не пустая строка, не длиннее 64 символов
- description - не пустая строка, не длиннее 1024 символов
- price - не пустая строка (которую можно перевести в целое число) или целое число, значения от 1 до 1000000

#### Возможные ответы:

- 201 - товар успешно сохранен
  - Пример ответа:
    ```python
    {"id": 112}
    ```
- 400 - запрос не прошел валидацию

`(POST) /api/v1/goods/:id/reviews/` - создать отзыв к товару, где :id - это id товара.
Формат запроса: `application/json`
Пример запроса:

```python
{
"text": "Best. Cheese. Ever.",
"grade": 9
}
```

Ограничения:

- Все поля обязательные
- text - не пустая строка, не длиннее 1024 символов
- grade - не пустая строка (которую можно перевести в целое число) или целое число, значения от 1 до 10

#### Возможные ответы:

- 201 - отзыв успешно сохранен
  - Пример ответа:
    ```python
    {"id": 95}
    ```
- 400 - запрос не прошел валидацию
- 404 - товара с таким id не существует.

`(GET) /api/v1/goods/:id/` - получить информацию о товаре, включая 5 последних отзывов.
Формат запроса: `application/json`
Ограничения:

- Если отзывов более 5 - вернуть последние 5. Порядок определять по id отзыва.
- Если отзывов менее 5 - вернуть сколько есть.
- Если отзывов на товар нет - вернуть пустой список.

#### Возможные ответы:

- `200 - OK`
  - Пример ответа:
    ```python
    {
    "id": 112,
    "title": "Сыр \"Российский\"",
    "description": "Очень вкусный сыр, да еще и российский.",
    "price": 100,
    "reviews": [{
    "id": 95,
    "text": "Best. Cheese. Ever.",
    "grade": 9
    }]
    }
    ```
- `404 - товара с таким id не существует`.

Вам необходимо реализовать только view классы и валидацию данных в них. Весь код должен находиться в файле view.py, который вы отправите на проверку. Реализовывать валидацию данных можно с использованием библиотек

- marshmallow http://marshmallow.readthedocs.io/en/latest/
- jsonschema http://python-jsonschema.readthedocs.io/en/latest/
  или с помощью класса Forms. Также в проекте установлен фреймворк для тестирования py.test https://docs.pytest.org/en/latest/ и реализован один тест в качестве примера. Мы рекомендуем вам попробовать реализовать свои тесты для самостоятельной проверки перед отправкой задания.