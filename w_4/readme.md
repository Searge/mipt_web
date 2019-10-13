# Полезные ссылки и дополнительные материалы
1. Пример простого CGI сервера. Стоит изучить для более глубокого понимания р    аботы web-сервера. https://habr.com/post/254621/
2. Шаблон проектирования MVC в рамках фреймворка Django. https://djangobook.c    om/model-view-controller-design-pattern/
3. Альтернативные фреймворки
    * Pyramid (http://www.pylonsproject.org/)
    * Falcon (https://falconframework.org/)
    * Twisted (https://twistedmatrix.com/)
    * Gevent (http://www.gevent.org/)

Туториал создание первого Django приложения (https://docs.djangoproject.com/en/1.11/intro/tutorial01/)

Созданный проект (https://github.com/alexopryshko/coursera_blog)

## Материалы по роутингу и устройство view:
- https://docs.djangoproject.com/en/1.11/ref/request-response/
- https://docs.djangoproject.com/en/1.11/topics/http/urls/
- https://docs.djangoproject.com/en/1.11/topics/http/views/
- https://docs.djangoproject.com/en/1.11/topics/http/decorators/

## Материалы по шаблонизации:
- https://docs.djangoproject.com/en/1.11/topics/templates/
- https://docs.djangoproject.com/en/1.11/ref/templates/builtins/
- https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/
- https://docs.djangoproject.com/en/1.11/ref/settings/

## Различия Django 1.11 и 2.0
В курсе рассмотрена версия `Django 1.11`, так как является стандартом технологии и многие существующие проекты написаны на более ранних версиях, которые несущественно отличаются от версии `1.11`.

Тем не менее, рассмотрим отличия версии `Django 2.0` от `Django 1.11`:

- `Django 2.0` поддерживает `Python 3.4`, `3.5` и `3.6`. `Django 1.11.x` является последней, которая поддерживает `Python 2.7`.
- Упрощенный `routing`. Новая функция `django.urls.path()` упрощает синтаксис роутинга. Например:

```python
# django 1.11
url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive)

# django 2.0
path('articles/<int:year>/', views.year_archive)
```

- Адаптированный под мобильные устройства раздел администрирования
- Window выражения

Полный список изменений - https://docs.djangoproject.com/en/2.0/releases/2.0/

## Документация Django (на английском)

- [Migrations](https://docs.djangoproject.com/en/1.11/topics/migrations/)
- [Aggregation](https://docs.djangoproject.com/en/1.11/topics/db/aggregation/)
- [Making queries](https://docs.djangoproject.com/en/1.11/topics/db/queries/)
- [Model field reference](https://docs.djangoproject.com/en/1.11/ref/models/fields/)
- [Models](https://docs.djangoproject.com/en/1.11/topics/db/models/)
- [Django ORM Cookbook](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/index.html)

Существуют альтернативные ORM:

* https://www.sqlalchemy.org/
* http://docs.peewee-orm.com/en/latest/

Но они обычно используются в связке с фрейворками, в которых нет встроенной ORM. Например, Flask