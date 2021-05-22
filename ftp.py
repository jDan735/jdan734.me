from server.server import app, file, template
import os

s = "/" if os.name == "posix" or os.name == "macos" else "\\"
PATH = os.path.abspath(os.path.dirname(__file__))


@app.route("/ftp/")
@app.route("/ftp/<query:path>")
@template("ftp.html")
async def ftp(request, query=None):
    path = f"{PATH}{s}static{request.path}"

    for i in os.walk(path):
        return {
            "path": request.path,
            "walk": i[1:],
            "status": "dev"
        }

    return await file(path)
