# 1. О шаблонизаторе, использование {{ }} в шаблонах
# https://www.youtube.com/watch?v=cFJqMXxVNsI&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U
# https://jinja.palletsprojects.com/en/2.11.x/
# Используеться в Flask и Django

# pip install jinja
# from jinja2 import Template

# from jinja2 import Template
#
# name = "Коля"
# age = 38
#
# tm = Template("Мне {{ a+10 }} лет и зовут {{ n.upper() }}")
# msg = tm.render(n=name, a=age)
#
# print(msg)

# {%%} - спецификатор шаблона
# {{}} - выражение для встаки конструкций Pthon  в шаблон
# {##} - блок комментариев
# # ## - строковый комментарий

# from jinja2 import Template
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# per = Person("Коля", 38)
#
# tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}")
# msg = tm.render(p=per)
#
# print(msg)

# from jinja2 import Template
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
# per = Person("Коля", 38)
#
# tm = Template("Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}")
# msg = tm.render(p=per)
#
# print(msg)

# from jinja2 import Template
#
# per = {'name': 'Коля', 'age': 38}
#
# #tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}")
# tm = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}")
# msg = tm.render(p=per)
#
# print(msg)

# 2. Экранирование и блоки raw, for, if

# from jinja2 import Template
#
# data = '''Модуль Jinja2 вместо
# определения {{ name }}
# подставляет соответствующее значение'''
#
# tm = Template(data)
# msg = tm.render(name='Николай')
# print(msg)

# {%raw%} ... {%endraw%}

# from jinja2 import Template
#
# data = '''{%raw%}Модуль Jinja2 вместо
# определения {{ name }}
# подставляет соответствующее значение{%endraw%}'''
#
# tm = Template(data)
# msg = tm.render(name='Николай')
# print(msg)

# <a href="Ссылка"></a> -> в HTML-документе воспринимаеться как Ссылка
# e - espase (экранирование)

# from jinja2 import Template
#
# link = '''В HTML документе ссылка определяется так:
# <a href="#">Ссылка</a>'''
#
# # tm = Template(link)
# tm = Template("{{link | e}}") # &lt;a href=&#34;#&#34;&gt;Ссылка&lt;/a&gt;
# msg = tm.render(link=link)
# print(msg)

# Можно записать проще! Устанавливаем Flask (он поддерживает escape, в новой Jinja не поддерживается!)

# from jinja2 import Template
# from flask import escape
#
# link = '''В HTML документе ссылка определяется так:
# <a href="#">Ссылка</a>'''
#
# msg = escape(link)
# print(msg)

# Блоки

# Ввражение for

# {% for <выражение>-%}
#     <повторяемый фрагмент>
# {% endfor %}

# from jinja2 import Template
#
# cities = [{'id': 1, 'city': 'Киев'},
#           {'id': 2, 'city': 'Львов'},
#           {'id': 3, 'city': 'Харьков'},
#           {'id': 4, 'city': 'Ровно'},
#           {'id': 5, 'city': 'Винница'}]
#
# link = '''<select name="cities">
# {% for c in cities -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% endfor -%}
# <select>'''
#
# # -% - убирает перенос строки!
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# Ввражение if

# {% if <условие>-%}
#     <фрагмент при истинности условия>
# {% endf %}

# from jinja2 import Template
#
# cities = [{'id': 1, 'city': 'Киев'},
#           {'id': 2, 'city': 'Львов'},
#           {'id': 3, 'city': 'Харьков'},
#           {'id': 4, 'city': 'Ровно'},
#           {'id': 5, 'city': 'Винница'}]
#
# link = '''<select name="cities">
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% elif c.city == 'Львов' -%}
#     <option>{{c['city']}}</option>
# {% else -%}
#     {{c['city']}}
# {% endif -%}
# {% endfor -%}
# <select>'''
#
# # -% - убирает перенос строки!
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# 3. Фильтры и макросы macro, call

# sum - вычисление суммы поля коллекции
# sum(iterable, attribute=None, start=0)

# from jinja2 import Template
#
# cars = [
#     {'model': 'Ауди', 'price': 23400},
#     {'model': 'Шкодв', 'price': 25200},
#     {'model': 'БМВ', 'price': 33000},
#     {'model': 'Фиат', 'price': 31100},
#     {'model': 'Рено', 'price': 21200},
# ]
#
# tpl = "Суммарная цена автомобилей: {{ cs | sum(attribute='price')}}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# from jinja2 import Template
#
# digs = [1, 2, 3, 4, 5]
#
# tpl = "Sum: {{ cs | sum}}"
# tm = Template(tpl)
# msg = tm.render(cs=digs)
# print(msg)

# https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters - список фильтров

# from jinja2 import Template
#
# cars = [
#     {'model': 'Ауди', 'price': 23400},
#     {'model': 'Шкодв', 'price': 25200},
#     {'model': 'БМВ', 'price': 33000},
#     {'model': 'Фиат', 'price': 31100},
#     {'model': 'Рено', 'price': 21200},
# ]
#
# tpl = "Максимальная цена автомобилей: {{ (cs | max(attribute='price')).price}}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Блок Filter

# {%filter<название фильтра>%}
# <фрагмент для применения фильтра>
# {%endfilter%}

# from jinja2 import Template
#
# persons = [
#     {"name": "Алксей", "old": 18, "weight": 78.5},
#     {"name": "Николай", "old": 20, "weight": 80},
#     {"name": "Дима", "old": 16, "weight": 75.5}
# ]
#
# tml = """
# {%- for u in users -%}
# {% filter upper %}{{u.name}}{% endfilter %}
# {% endfor -%}
# """
#
# tm = Template(tml)
# msg = tm.render(users=persons)
# print(msg)

# Макроопределения
# DRY - Don`t Repeat Yourself (не повторяйся)

# from jinja2 import Template
#
# html = """
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# Вложенные макросы

# {% call[(параметры)] <вызов макроса> %}
# <вложенный шаблон>
# {% endcall%}

# from jinja2 import Template
#
# persons = [
#     {"name": "Алксей", "old": 18, "weight": 78.5},
#     {"name": "Николай", "old": 20, "weight": 80},
#     {"name": "Дима", "old": 16, "weight": 75.5}
# ]
#
# html = """
# {% macro list_users(list_of_user) -%}
# <ul>
# {%- for u in list_of_user -%}
#     <li>{{u.name}} {{caller(u)}}</li>
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#     <li>age: {{user.old}}</li>
#     <li>weight: {{user.weight}}</li>
#     </ul>
# {% endcall -%}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in users -%}
#     <li>{{u.name}} {{caller(u)}}
# {%- endfor %}
# </ul>
# {%- endmacro %}
# _________________________________
#
# { call(user) list_users(users) %}
#     <ul>
#     <li>age: {{user.age}}
#     <li>weight: {{user.weight}}
#     </ul>
# {% endcall -%}

# 4. Загрузчики шаблонов - FileSystemLoader, PackageLoader, DictLoader, FunctionLoader

# https://jinja.palletsprojects.com/en/3.0.x/api/

# FileSystemLoader - для загрузки из файловой системы
# PackageLoader - для загрузки шаблонов из пакета
# DictLoader - для загрузки шаблонов из словаря
# FunctionLoader - для загрузки на основе функции
# PrefixLoader - загрузчик, содержащий словарь для постраения подкаталогов
# ChoiceLoader - загрузчик, содержащий список других загрузчиков
# (если один не сработает, выбирается следующий)
# ModuleLoader - загрузчик для скомпилированных шаблонов

