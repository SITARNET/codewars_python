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

from jinja2 import Template

cities = [{'id': 1, 'city': 'Киев'},
          {'id': 2, 'city': 'Львов'},
          {'id': 3, 'city': 'Харьков'},
          {'id': 4, 'city': 'Ровно'},
          {'id': 5, 'city': 'Винница'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 3 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == 'Львов' -%}
    <option>{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
<select>'''

# -% - убирает перенос строки!

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)