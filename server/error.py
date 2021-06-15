from sanic.exceptions import NotFound
from .server import app, page, template


@app.exception(NotFound)
@template("404.html")
async def not_found(request, exception):
    return {}


@app.exception(Exception)
@template("500.html")
async def internal_error(request, exception):
    return {"error": exception}


@app.route('/0')
async def nol(request):
    return 0 / 0
