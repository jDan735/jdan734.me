from .error import app
from bs4 import BeautifulSoup
from flask import render_template, Markup

import requests


# @app.route("/habr/<int:id_>")
# def habr(id_):
#     a = habr_page(id_)
#     return '<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16" /><link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32" /><link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" /><link rel="stylesheet" href="/css/style.css?v=2.8.9" /><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><body class="index habr">' + a[0] + a[1] + "</body>"

@app.route("/habr/<int:id_>")
def habr(id_):
    a = habr_page(id_)
    return render_template("habr.html",
                           title=a[0],
                           content=Markup(a[1]))


def habr_page(id_):
    r = requests.get(f"https://habr.com/ru/post/{id_}/")
    soup = BeautifulSoup(r.text, "lxml")
    page = []

    page.append(soup.find("h1").span.text)

    content = soup.findAll("div", {"id": "post-content-body"})[0]

    for tag in content.findAll("code"):
        tag["class"] = "hljs"

    page.append(str(content))
    return page
