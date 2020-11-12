from .server import app


@app.route("/api")
def api():
    return {
        "ban": True,
        "ban_count": 1488,
        "rzaka_time": 848393938347292929647492918363739304964682010,
        "pi": 3.14
    }


@app.route("/api/getbanlist")
def api_getbanlist():
    return {
        "chat": "@katz_bot",
        "ybane": [
            "偽のキティ",
            "Малой",
            "John Doe",
            "Combot",
            "Егор Жуков",
            "Рамон Гастаев",
            "Евгений Мишин",
            "Timur Gadiev",
            "dima",
            "𝕬. 𝕸𝖆𝖙𝖛𝖎𝖊𝖛𝖘𝖐𝖞",
            "РРРЯЯЯ",
            "Александр Гомель",
            "Kotoeba",
            "Иван",
            "Анатолий УберКац",
            "Blaton",
            "Власть шизов"
        ]
    }


@app.route("/kanobu/server")
def kanobu_server():
    return {
        "game": "kanobu",
        "users": ["ban", "obama", "3nr3"],
        "time": 1,
        "ban": True
    }


@app.route("/kanobu/server/<user>")
def kanobu_server_user(user):
    return {
        "user": user
    }
