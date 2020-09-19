from flask import Flask
from wikipedia import Wikipedia
app = Flask(__name__)


def page(file_name):
    with open(file_name, encoding="utf-8") as file:
        return file.read()


@app.route('/')
def index():
    return page("index.html")


@app.route('/obama')
def sosat():
    return "sosat"


@app.route('/kanobu')
def kanobu():
    return page("kanobu.html")


@app.route('/timer')
def timer():
    return page("timer.html")


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
    wiki = Wikipedia("ru")
    search = wiki.search(page_name)

    if search == -1:
        with open("404.html", encoding="utf-8") as index:
            return index.read()

    head = '<link rel="icon" type="image/png" href="/static/favicon-16x16.png" sizes="16x16" /><link rel="icon" type="image/png" href="/static/favicon-32x32.png" sizes="32x32" /><link rel="icon" type="image/png" href="/static/favicon-96x96.png" sizes="96x96" /><link rel="stylesheet" href="/static/css/style.css?v=1.5.7" /><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />'

    h1 = f'<h1 class=wiki>{makeBelarus(search[0][0])}</h1>'
    page = makeBelarus(str(wiki.getPage(search[0][0], -1)))
    title = f'<title>{makeBelarus(search[0][0])}</title>'
    style = '<link rel="stylesheet" href="/static/css/style.css?v=1.4.0"/><link rel="stylesheet" href="/static/css/wiki.css?v=1.8.2"/>'

    image_url = wiki.getImageByPageName(search[0][0], 400)

    page_open = "<div class=page>"

    if image_url == "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/400px-Flag_of_Belarus.svg.png":
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg/400px-Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg.png"

    if image_url == -1:
        img = ""

    else:
        full_image_url = wiki.getImageByPageName(search[0][0])

        if full_image_url == "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/1000px-Flag_of_Belarus.svg.png":
            full_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg/1000px-Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg.png"

        img = f'<a href="{full_image_url}"><img src="{image_url}"></a>'

    result = head + style + title + img + page_open + h1 + page + "</div>"

    return result


@app.errorhandler(404)
def not_found(error):
    return page("404.html")


@app.errorhandler(505)
def not_found_shizha(error):
    return "Не сюда)"


@app.route('/lorem')
def lorem():
    return page("lorem.html")


if __name__ == '__main__':
    app.run(port=5050)
