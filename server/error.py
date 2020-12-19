from server.server import app, page


@app.errorhandler(404)
def not_found(error):
    return page("404.html")


@app.errorhandler(500)
def internal_error(error):
    return page("500.html")


@app.route('/0')
def nol():
    return 0 / 0


@app.errorhandler(505)
def not_found_shizha(error):
    return "Не сюда)"
