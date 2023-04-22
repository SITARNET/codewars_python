from jinja2 import Environment, FileSystemLoader

subs = ["Математика", "Физика", "Информатика", "Украинский"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.htm')
output = template.render(list_table=subs)

print(output)