from .server import app, page

from sanic.response import json
from sanic.exceptions import NotFound


@app.route("/<query>")
async def getPage(request, query):
    try:
        if query[-5:] == ".html":
            path = query

        elif query[-4:] == ".htm":
            path = f"{query}l"

        else:
            path = f"{query}.html"

        return page(path)

    except Exception:
        raise NotFound("Not found page")
