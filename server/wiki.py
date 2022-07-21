from sanic.exceptions import NotFound
from sanic.response import redirect

from wikipya.aiowiki import Wikipya
from .server import app, template#, page, template, json


WGR_FLAG = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb" +
    "/8/85/Flag_of_Belarus.svg/1000px-Flag_of_Belarus.svg.png"
)

WRW_FLAG = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb" +
    "/5/50/Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg" +
    "/1000px-Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg.png"
)


@app.route("/wiki")
@template("wiki.html")
async def wikimain(response):
    title = response.args.get("title")
    lang = response.args.get("lang")

    if title is None:
        return {"status": "dev"}
    else:
        return await wiki(response=response, name=title, lang=lang)


def makeBelarus(text):
    namelist = [
        ["Белоруссия", "Беларусь"],
        ["Белоруссии", "Беларуси"],
        ["Беларуссию", "Беларусь"],
        ["Белоруссией", "Беларусью"],
        ["Белоруссиею", "Беларусью"],


        ["Белору́ссия", "Белару́сь"],
        ["Белору́ссии", "Белару́си"],
        ["Белору́ссию", "Белару́сь"],
        ["Белору́ссией", "Белару́сью"],
        ["Белору́ссиею", "Белару́сью"]
    ]

    for name in namelist:
        text = text.replace(*name)

    return text


@app.route('/wiki/<name>')
async def wiki_handler(response, name=None):
#    return await wiki(response, name)
    return redirect(f"/wiki?title={name}")


@template("wikipage.html")
async def wiki(response=None, name=None, lang=None):
    wiki = Wikipya("ru" if lang is None else lang).get_instance()
    search = await wiki.search(name)

    if search == -1:
        raise NotFound()

    page = await wiki.page(search[0], 999999999999999)

    if page == -1:
        text = ""

    elif str(page) == "":
        text = ""

    else:
        page.blockList = [["table", {"class": "infobox"}],
                          ["ol", {"class": "references"}],
                          ["link"], ["style"], ["img"],
                          ["div", {"class": "tright"}],
                          ["table", {"class": "noprint"}],
                          ["div", {"class": "plainlist"}],
                          ["table", {"class": "sidebar"}],
                          ["span", {"class": "mw-ext-cite-error"}]]
        text = makeBelarus(page.parsed)

    try:
        image = await page.image()
        image = image.source

    except (AttributeError, NotFound):
        image = -1

    if image == WGR_FLAG:
        image = WRW_FLAG

    text = text.replace("<body>", "") \
                .replace("</body>", "") \
                .replace("<html>", "") \
                .replace("</html>", "")

    return {
        "title": makeBelarus(search[0].title),
        "content": text,
        "image_url": image
    }
