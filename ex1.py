from jinja2 import Environment, FileSystemLoader, FunctionLoader

person = [
    {"name": "Алексей", "old": 18, "weigth": 78.5},
    {"name": "Николай", "old": 28, "weigth": 82.3},
    {"name": "Иван", "old": 33, "weigth": 94.0}
]

def loadTpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''

# file_loader = FileSystemLoader('templates')
file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(u=person[0])

print(msg)