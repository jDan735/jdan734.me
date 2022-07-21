from .server import app, templates

from aiohttp import ClientSession
from bs4 import BeautifulSoup

from fastapi import Request
from fastapi.responses import HTMLResponse


@app.get("/habr/{id_}", response_class=HTMLResponse)
async def habr_test(request: Request, id_: int):
    async with ClientSession() as session:
        res = await session.get(f"https://habr.com/ru/post/{id_}/")
        soup = BeautifulSoup(await res.text(), 'html.parser')

    content = soup.find("div", {"id": "post-content-body"})

    for tag in content.findAll("code"):
        tag["class"] = "hljs"

    return templates.TemplateResponse(
        "habr.html",
        {
            "request": request,
            "title": soup.find("h1").span.text,
            "content": str(content)
        }
    )
