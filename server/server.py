from sanic.response import html, json, text, file
from jinja2 import Template, Environment, FileSystemLoader

import sys

sys.path.append('../')
from app import app
from .db import notes, events, pidorstats, warns


def page(name):
    return sopen(name, "html/{name}", wrapper=html)


def template(name):
    def outer(func):
        async def wrapper(*args, **kwargs):
            params = await func(*args, **kwargs)

            if not isinstance(params, dict):
                return params

            env = Environment(loader=FileSystemLoader("templates"))
            template = env.get_template(name)

            return html(template.render(**params))

        return wrapper

    return outer


def sopen(name, path_template="templates/{name}", wrapper=lambda x: x):
    with open(path_template.format(name=name), encoding="utf-8") as f:
        return wrapper(f.read())


# FTP_TEMPLATE = Template(template("ftp.html"))

@app.route("/old")
@template("index_old.html")
async def stats(request):
    return {
        "users": len(await events.get_unique_users()),
        "notes": len(await notes.select()),
        "warns": len(await warns.select())
    }


@app.route("/bootstrap")
@template("bootstrap.html")
async def bs4(request):
    return {}


@app.route("/lorem")
@template("lorem.html")
async def bs4(request):
    return {}


@app.route("/")
@template("index.html")
async def index(request):
    return {
        "status": "dev"
    }


@app.route("/rss")
async def rss(request):
    return await file(
        "templates/rss.xml",
        headers={"Content-Type": "application/rss+xml"}
    )
