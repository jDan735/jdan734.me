from server.server import app, page


@app.route("/")
def mainPage():
    return page("index.html")


@app.route("/<query>")
def getPage(query):
    try:
        if query[-5:] == ".html":
            path = query

        elif query[-4:] == ".htm":
            path = f"{query}l"

        else:
            path = f"{query}.html"

        return page(path)

    except FileNotFoundError:
        return page("404.html")
