from sanic.exceptions import NotFound
from .server import app, page


@app.exception(NotFound)
async def not_found(request, exception):
    return page("404.html")


# @app.errorhandler(500)
# async def internal_error(error):
#     return page("500.html")


@app.route('/0')
async def nol(request):
    return 0 / 0
