from .server import app, page

from sanic.response import json


@app.route("/")
async def mainPage(request):
    return page("index.html")


@app.route("/<query>")
async def getPage(request, query):
    print(query)
    try:
        if query[-5:] == ".html":
            path = query

        elif query[-4:] == ".htm":
            path = f"{query}l"

        else:
            path = f"{query}.html"

        return page(path)

    except FileNotFoundError:
        return page("404.html")
