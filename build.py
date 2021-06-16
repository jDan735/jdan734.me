from jinja2 import Template, Environment, FileSystemLoader
from os import listdir

# import htmlmin

for name in listdir("templates"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(name)

    with open(name, "w", encoding="UTF-8") as file:
        # html = htmlmin.minify(template.render(),
        #                       remove_empty_space=True,
        #                       remove_comments=True)
        html = template.render()
        file.write(html)
