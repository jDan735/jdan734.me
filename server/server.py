from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import pymemeru


exceptions = {
    404: lambda r, e: get_template(r, "404.html", {}),
    500: lambda r, e: get_template(r, "500.html", {})
}

app = FastAPI(exception_handlers=exceptions)
templates = Jinja2Templates(directory="templates")

app.mount("/css", StaticFiles(directory="css"), name="static_css")
app.mount("/images", StaticFiles(directory="images"), name="static_images")
app.mount("/js", StaticFiles(directory="js"), name="static_js")
# from .db import notes, events, pidorstats, warns


def template(name):
    def outer(func):
        async def wrapper(*args, **kwargs):
            request, params = await func(*args, **kwargs)
            return templates.TemplateResponse(name, {"request": request, **params})

        return wrapper

    return outer


def get_template(request, name, params):
    print(params)

    return templates.TemplateResponse(
        name,
        {
            "request": request,
            **params
        }
    )


def sopen(name, path_template="templates/{name}", wrapper=lambda x: x):
    with open(path_template.format(name=name), encoding="utf-8") as f:
        return wrapper(f.read())


# FTP_TEMPLATE = Template(template("ftp.html"))


@app.route("/bootstrap")
async def bs4(request: Request):
    return get_template(request, "bootstrap.html", {})


@app.route("/lorem")
async def bs4(request: Request):
    return get_template(request, "lorem.html", {})


@app.route("/rss")
async def rss(request: Request, response_class=Response):
    return get_template(request, "rss.xml", {})


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return get_template(request, "index.html", {
        "status": "dev"
    })


@app.get("/new", response_class=HTMLResponse)
async def index(request: Request):
    return get_template(request, "index_new.html", {
        "status": "dev"
    })


@app.get("/memepedia/{page_name}", response_class=HTMLResponse)
async def index(request: Request, page_name: str):
    page = await pymemeru.page(page_name)

    return get_template(request, "memepedia_page.html", {
        "status": "dev",
        "text": str(page.cleared_text),
        "title": page.title,
        "img": page.main_image,
        "trending": (await pymemeru.popular())[:10],
        "time_publication": page.published_at,
        "author_name": page.author_name,
        "comments": page.comments,
        "views": page.views
    })


@app.get("/memepedia", response_class=HTMLResponse)
async def index(request: Request):
    return get_template(request, "memepedia.html", {
        "status": "dev",
        "trending": await get_popular()
    })


async def get_popular() -> list:
    trends = await pymemeru.popular()

    trends_new = []

    for ind, __ in enumerate(trends):
        a = trends[ind:ind + 4]

        try:
            trends.remove(a[1])
            trends.remove(a[2])
            trends.remove(a[3])
        except:
            pass

        trends_new.append(a)

    return trends_new
