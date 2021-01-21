from flask import request, render_template, Markup, Response
from server.server import app, page
import os

s = "/" if os.name == "posix" or os.name == "macos" else "\\"


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


@app.route('/ftp/code/jdan734-bot')
def code_bot():
    return ftp("/code/jdan734-bot")


@app.route('/ftp/code/jdan734-bot/flake8')
def code_bot_flake8():
    return ftp("/code/jdan734-bot/flake8")


@app.route('/ftp/test')
def test3():
    return ftp('/test')


@app.route('/ftp')
@app.route('/ftp/')
def ftp1():
    return ftp()


def ftp(path=""):
    file_path = os.path.abspath(os.path.dirname(__file__))
    this = None

    fp = f"{s}static{s}ftp{s}{path}"

    for i in os.walk(file_path + fp):
        this = i[1:]

        break

    else:
        try:
            return
            ext = path.split("/")[-1].split(".")[-1]
            mimetypes = {
                "css": "text/css",
                "html": "text/html",
                "js": "application/javascript",
                "png": "image/png",
                "gif": "image/gif",
                "jpg": "image/jpeg"
            }
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
        [["js"], "☕️", "text/javascript"],
        [["txt"], "🗒", "text/plain"]
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
        h1 = "Index of " + fp.replace(f"{s}static", "") \
                             .replace(s, "/") \
                             .replace("//", "/")

    return render_template("ftp.html",
                           title=h1,
                           content=Markup("<table>" + folders_table + folders +
                                          files_table + files))
