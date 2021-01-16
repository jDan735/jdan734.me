from flask import request, render_template, Markup
from wikipya.core import Wikipya
from server.server import app, page


@app.route("/wiki")
def wikimain():
    title = request.args.get("title", type=str)
    if title is None:
        return page("wiki.html")
    else:
        return wiki(title)


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


@app.route('/wiki/<page_name>')
def wiki(page_name):
    wiki = Wikipya("ru")
    search = wiki.search(page_name)

    if search == -1:
        with open("404.html", encoding="utf-8") as index:
            return index.read()

    page = makeBelarus(str(wiki.getPage(search[0][0], -1)))
    image_url = wiki.getImageByPageName(search[0][0], 400)

    if image_url != -1:
        image_url = image_url["source"]
        full_image_url = wiki.getImageByPageName(search[0][0])

        if image_url == "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/400px-Flag_of_Belarus.svg.png":
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg/400px-Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg.png"

        if full_image_url == "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/1000px-Flag_of_Belarus.svg.png":
            full_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg/1000px-Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg.png"

        page = page.replace("<body>", "") \
                   .replace("</body>", "") \
                   .replace("<html>", "") \
                   .replace("</html>", "")
    else:
        image_url = ""

    print(image_url)

    return render_template("wikipage.html",
                           title=makeBelarus(search[0][0]),
                           content=Markup(page),
                           image_url=image_url)
