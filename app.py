from flask import Flask, Response
from wikipedia import Wikipedia
import os
import requests
from bs4 import BeautifulSoup
app = Flask(__name__, static_url_path="/")


def page(file_name):
    with open(file_name, encoding="utf-8") as file:
        return file.read()


pages = {
    "index": page("index.html"),
    "kanobu": page("kanobu.html"),
    "timer": page("timer.html"),
    "404": page("404.html"),
    "lorem": page("lorem.html"),
    "test": page("test.html"),
    "ligatures": page("ligatures.html"),
    "ftp": page("ftp.html")
}


@app.route("/")
def index():
    return pages["index"]


@app.route("/api")
def api():
    return {
        "ban": True,
        "ban_count": 1488,
        "rzaka_time": 848393938347292929647492918363739304964682010,
        "pi": 3.14
    }


@app.route("/habr/<int:id_>")
def habr(id_):
    a = habr_page(id_)
    return '<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16" /><link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32" /><link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" /><link rel="stylesheet" href="/css/style.css?v=2.7.7" /><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><body class="index habr">' + a[0] + a[1] + "</body>"


@app.route("/api/getbanlist")
def api_getbanlist():
    return {
        "chat": "@katz_bot",
        "ybane": [
            "偽のキティ",
            "Малой",
            "John Doe",
            "Combot",
            "Егор Жуков",
            "Рамон Гастаев",
            "Евгений Мишин",
            "Timur Gadiev",
            "dima",
            "𝕬. 𝕸𝖆𝖙𝖛𝖎𝖊𝖛𝖘𝖐𝖞",
            "РРРЯЯЯ",
            "Александр Гомель",
            "Kotoeba",
            "Иван",
            "Анатолий УберКац",
            "Blaton",
            "Власть шизов"
        ]
    }


@app.route("/kanobu/server")
def kanobu_server():
    return {
        "game": "kanobu",
        "users": ["ban", "obama", "3nr3"],
        "time": 1,
        "ban": True
    }


@app.route("/kanobu/server/<user>")
def kanobu_server_user(user):
    return {
        "user": user
    }


@app.route("/demo")
def test():
    return page("demo.html")


@app.route("/neo_kanobu")
def neo_kanobu():
    return page("neo_kanobu.html")


@app.route("/test")
def demo():
    return pages["test"]


@app.route('/obama')
def sosat():
    return "sosat"


@app.route('/kanobu')
def kanobu():
    return pages["kanobu"]


@app.route('/ligatures')
def ligatures():
    return pages["ligatures"]


@app.route('/timer')
def timer():
    return pages["timer"]


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

    head = '<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16" /><link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32" /><link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" /><link rel="stylesheet" href="/css/style.css?v=2.7.8" /><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />'

    h1 = f'<body class=index><h1 class="wiki header">{makeBelarus(search[0][0])}</h1>'
    page = makeBelarus(str(wiki.getPage(search[0][0], -1)))
    title = f'<title>{makeBelarus(search[0][0])}</title>'
    style = '<link rel="stylesheet" href="/css/style.css?v=2.7.7"/><link rel="stylesheet" href="/css/wiki.css?v=1.9.3"/>'

    image_url = wiki.getImageByPageName(search[0][0], 400)

    page_open = '<div class="page demo">'

    if image_url == "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/400px-Flag_of_Belarus.svg.png":
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg/400px-Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg.png"

    if image_url == -1:
        img = ""

    else:
        full_image_url = wiki.getImageByPageName(search[0][0])

        if full_image_url == "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/1000px-Flag_of_Belarus.svg.png":
            full_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg/1000px-Flag_of_Belarus_%281918%2C_1991%E2%80%931995%29.svg.png"

        img = f'<a class="wiki-image" href="{full_image_url}"><img src="{image_url}"></a>'

        page = page.replace("<body>", "") \
                   .replace("</body>", "") \
                   .replace("<html>", "") \
                   .replace("</html>", "")

    result = head + style + title + img + h1 + page_open + page + "</div></body>"

    return result


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f"{round(num, 2)} {x}"
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


@app.route('/ftp/test/ban')
def testban():
    return ftp("/test/ban")


@app.route('/ftp/test/test2')
def test2():
    return ftp("/test/test2")


@app.route('/ftp/honka')
def honka():
    return ftp("/honka")


@app.route('/ftp/code')
def code():
    return ftp("/code")


@app.route('/ftp/code/tel-parser')
def code_tel_parser():
    return ftp("/code/tel-parser")


@app.route('/ftp/test')
def test3():
    return ftp('/test')


@app.route('/ftp')
@app.route('/ftp/')
def ftp1():
    return ftp()


def ftp(path=""):
    file_path = os.path.abspath(os.path.dirname(__file__))
    s = "/" if os.name == "posix" or os.name == "macos" else "\\"
    a = ""
    this = None

    fp = f"{s}static{s}ftp{s}{path}"

    for i in os.walk(file_path + fp):
        this = i[1:]

        break

    else:
        try:
            return
            print(path)
            ext = path.split("/")[-1].split(".")[-1]
            print(ext)
            mimetypes = {
                "css": "text/css",
                "html": "text/html",
                "js": "application/javascript",
                "png": "image/png",
                "gif": "image/gif",
                "jpg": "image/jpeg"
            }
            print(mimetypes[ext])
            # return send_from_directory("ftp", f"test{s}style.css")
            return Response(page(file_path + fp), mimetype="image/svg+xml")
            # return page(file_path + fp).replace("\n", "<br>")
        except:
            return 404

    went = fp.replace(s + 'static', '')
    went = went.replace(s, "/").replace("//", "/")
    went = went.split("/")[0:-1]
    went = "/".join(went)

    folders = ""
    files = ""

    if path != "":
        folders += f'<tr><td>📂</td><td><a class=emoji href={went}>../</a></td><td>inode/directory</td><td>-</td></tr>'

    icons = [
        [["png"], "🖼", "image/png"],
        [["webp"], "🖼", "image/webp"],
        [["svg"], "🖼", "image/svg+xml"],
        [["jpeg", "jpg"], "🖼", "image/jpeg"],
        [["license"], "📖", "text/plain"],
        [["procfile"], "🤖", "text/plain"],
        [["css"], "💅", "text/css"],
        [["py"], "🐍", "text/x-python"],
        [["md"], "📝", "text/markdown"],
        [["js"], "☕️", "text/javascript"]
    ]

    folders_table = "<tr><td>😀</td><td>Name</td><td>MIME-type</td><td>Size</td></tr>"

    for b in this[0]:
        folders += f'<tr><td>📂</td><td><a class=emoji href="{fp.replace(s + "static", "")}{s}{b}">{b}/</a></td><td>inode/directory</td><td>-</td></tr>'

    if folders == "":
        folders_table = ""

    files_table = ""

    for b in this[1]:
        file_icon = "📄"

        for icon in icons:
            ext = b.split(".")[-1].lower()
            for type_ in icon[0]:
                if ext == type_:
                    file_icon = icon[1]
                    file_type = icon[2]
                    break

        path = (fp + s + b).replace("\\", "/") \
                           .replace("/static", "") \
                           .replace("//", "/")

        size = file_size(f"{os.path.dirname(os.path.abspath(__file__))}/static{path}".replace("/", s))

        files += f"<tr><td>{file_icon}</td><td><a class=emoji href={path}>{b}</a></td><td>{file_type}</td><td>{size}</td></tr>"

    if files == "":
        files_table = ""

    if path == "":
        h1 = "Index of /ftp"

    else:
        h1 = "Index of " + fp.replace(f"{s}static", "").replace(s, "/").replace("//", "/")

    return f'<!DOCTYPE html><html><head><link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16"><link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32"><link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96"><link rel="stylesheet" href="/css/style.css?v=2.7.9"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>FTP</title></head><body class="index ftp"><h1 class=header>{h1}</h1><div><table>' + folders_table + folders + files_table + files + "</ul></div></body></html>"


@app.errorhandler(404)
def not_found(error):
    return pages["404"]


def habr_page(id_):
    r = requests.get(f"https://habr.com/ru/post/{id_}/")
    soup = BeautifulSoup(r.text, "lxml")
    page = []

    page.append("<h1 class=header>" + soup.find("h1").span.text + "</h1>")
    page.append(str(soup.findAll("div", {"id": "post-content-body"})[0]))
    return page


@app.errorhandler(505)
def not_found_shizha(error):
    return "Не сюда)"


@app.route('/lorem')
def lorem():
    return pages["lorem"]


if __name__ == '__main__':
    app.run(port=5050)
