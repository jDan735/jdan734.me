from sanic import Sanic
from sanic.response import html
from sanic.exceptions import NotFound


app = Sanic(__name__)
app.static('image', 'image')
app.static('html', 'html')
app.static('css', 'css')
app.static('old', 'old')
app.static('js', 'js')


def page(name):
    return sopen(name, "{name}", wrapper=html)


def sopen(name, path_template="templates/{name}", wrapper=lambda x: x):
    with open(path_template.format(name=name), encoding="utf-8") as f:
        return wrapper(f.read())


@app.route("/<query>")
async def getPage(request, query):
    try:
        if query[-5:] == ".html":
            path = query

        elif query[-4:] == ".htm":
            path = f"{query}l"

        else:
            path = f"{query}.html"

        return page(path)

    except Exception:
        raise NotFound("Not found page")


if __name__ == '__main__':
    app.run(port=5050) # debug=True
