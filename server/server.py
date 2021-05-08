from sanic.response import html
from jinja2 import Template

import sys

sys.path.append('../')
from app import app
from .db import notes, events, pidorstats, warns


def page(name):
    return sopen(name, "html/{name}", wrapper=html)


def template(name):
    return sopen(name)


def template(name):
    def outer(func):
        async def wrapper(*args, **kwargs):
            temp = Template(sopen(name))
            return html(temp.render(**await func(*args, **kwargs)))

        return wrapper

    return outer


def sopen(name, path_template="templates/{name}", wrapper=lambda x: x):
    with open(path_template.format(name=name), encoding="utf-8") as f:
        return wrapper(f.read())


# FTP_TEMPLATE = Template(template("ftp.html"))

@app.route("/stats")
@template("index.html")
async def stats(request):
    return {
        "users": len(await events.get_unique_users()),
        "notes": len(await notes.select()),
        "warns": len(await warns.select())
    }
