from server.server import app, page


@app.route("/repo/")
def repo():
    return page("../static/repo/index.html")


@app.route("/repo/x86_gcc2/")
def repo_gcc2():
    return page("../static/repo/x86_gcc2/index.html")
