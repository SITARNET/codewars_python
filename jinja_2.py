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

from jinja2 import Template

per = {'name': 'Коля', 'age': 38}

#tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}")
tm = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}")
msg = tm.render(p=per)

print(msg)

