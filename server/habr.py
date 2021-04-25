from .server import app, template

from aiohttp import ClientSession
from bs4 import BeautifulSoup


@app.route("/habr/<id_>")
@template("habr.html")
async def habr(request, id_):
    async with ClientSession() as session:
        res = await session.get(f"https://habr.com/ru/post/{id_}/")
        soup = BeautifulSoup(await res.text(), 'html.parser')

    content = soup.find("div", {"id": "post-content-body"})

    for tag in content.findAll("code"):
        tag["class"] = "hljs"

    return {
        "title": soup.find("h1").span.text,
        "content": str(content)
    }
