from jinja2 import Environment, FileSystemLoader, FunctionLoader

person = [
    {"name": "Алексей", "old": 18, "weigth": 78.5},
    {"name": "Николай", "old": 28, "weigth": 82.3},
    {"name": "Иван", "old": 33, "weigth": 94.0}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.htm')
msg = tm.render(domain='http://site.com', title='Про Jinja')

print(msg)