from .server import app, pages, page


@app.route("/")
def index():
    return pages["index"]


@app.route("/demo")
def test():
    return page("demo.html")


@app.route("/bot")
def bot():
    return page("bot.html")


@app.route("/neo_kanobu")
def neo_kanobu():
    return page("neo_kanobu.html")


@app.route("/test")
def demo():
    return pages["test"]


@app.route('/obama')
def sosat():
    return "sosat"


@app.route('/kanobu')
def kanobu():
    return pages["kanobu"]


@app.route('/ligatures')
def ligatures():
    return pages["ligatures"]


@app.route('/timer')
def timer():
    return pages["timer"]


@app.route('/lorem')
def lorem():
    return pages["lorem"]
