from .server import app, page


@app.route("/")
def index():
    return page("index.html")


@app.route("/demo")
def test():
    return page("demo.html")


@app.route("/bot")
def bot():
    return page("bot.html")


@app.route("/test")
def demo():
    return page("test.html")


@app.route('/kanobu')
def kanobu():
    return page("kanobu.html")


@app.route('/ligatures')
def ligatures():
    return page("ligatures.html")


@app.route('/lorem')
def lorem():
    return page("lorem.html")
