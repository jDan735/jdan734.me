from server.server import app, page, html, template
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
async def testban(request):
    return await ftp("/test/ban")


@app.route('/ftp/test/test2')
async def test2(request):
    return await ftp("/test/test2")


@app.route('/ftp/honka')
async def honka(request):
    return await ftp("/honka")


@app.route('/ftp/code')
async def code(request):
    return await ftp("/code")


@app.route('/ftp/code/tel-parser')
async def code_tel_parser(request):
    return await ftp("/code/tel-parser")


@app.route('/ftp/code/jdan734-bot')
async def code_bot(request):
    return await ftp("/code/jdan734-bot")


@app.route('/ftp/code/jdan734-bot/flake8')
async def code_bot_flake8(request):
    return await ftp("/code/jdan734-bot/flake8")


@app.route('/ftp/test')
async def ftp2(request):
    return await ftp('/test')


@app.route("/ftp")
async def ftp4(request):
    return await ftp()


@template("ftp.html")
async def ftp(path=""):
    print("test")
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

    folders_table = "<thead><td>😀</td><td>Name</td><td>MIME-type</td><td>Size</td></thead>"

    for b in this[0]:
        path_ = (fp.replace(s + "static", "") + s + b).replace("\\\\", "\\") \
                                                      .replace("//", "/")
        folders += f'<tr><td>📂</td><td><a class=emoji href="{path_}">{b}/</a></td><td>inode/directory</td><td>-</td></tr>'

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

    return {
        "title": h1,
        "content": "<table>" + folders_table + folders + files_table + files
    }
