from flask import request
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

    head = '<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16" /><link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32" /><link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" /><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />'

    h1 = f'<body class=index><h1 class="wiki header">{makeBelarus(search[0][0])}</h1>'
    page = makeBelarus(str(wiki.getPage(search[0][0], -1)))
    title = f'<title>{makeBelarus(search[0][0])}</title>'
    style = '<link rel="stylesheet" href="/css/style.css?v=2.9.9"/><link rel="stylesheet" href="/css/wiki.css?v=1.9.3"/>'

    image_url = wiki.getImageByPageName(search[0][0], 400)

    page_open = '<div class="page demo">'

    if image_url == -1:
        img = ""

    else:
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

    result = head + style + title + '<nav><ul><li><a class="home" href="/">Home</a></li><li><a class="lorem" href="/lorem">Lorem</a></li><li><a class="wiki active" href="/wiki/wikipedia">Wikipedia</a></li><li><a class="ftp-menu" href="/ftp">FTP</a></li><li><a class="bot" href="/bot">Bot</a></li><li><a class="kanobu" href="/kanobu">Kanobu</a></li></ul></nav><header style="background: url(' + full_image_url["source"] + ') no-repeat center fixed" class="header-image"><section>' + h1 + "</section></header>" + page_open + page + "</div></body>"

    return result
