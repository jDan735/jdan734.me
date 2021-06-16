from jinja2 import Template, Environment, FileSystemLoader
from os import listdir

print(listdir("templates"))

for name in listdir("templates"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(name)

    with open(name, "w", encoding="UTF-8") as file:
        file.write(template.render())
    # print(template.render())
