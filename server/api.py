from server.server import app, page, conn
from flask import request, jsonify
from random import randint


params = {}
arguments = [
    ["action", str],
    ["limit", int],
    ["format", str],
    ["username", str],
    ["gamer", int],            # Gamer's choice
    ["bot", int],              # Bot's choice
    ["result", int]
]


class APIError:
    def __init__(self, text):
        self.json = {"error": text}


class jDan734api:
    def __init__(self):
        pass

    def ban(self, **kwargs):
        return {"ban": True, "date": "always has been"}

    def random(self, **kwargs):
        limit = 10 if kwargs["limit"] is None else kwargs["limit"]

        if limit > 10000:
            return APIError("Limit is bigger is 10000").json

        return {"number": randint(0, limit)}

    def testdb(self, **kwargs):
        return {
            "status": conn.status
        }

    def showdb(self, **kwargs):
        cur = conn.cursor()
        cur.execute("SELECT * FROM games;")
        e = cur.fetchall()
        return e

    def addtodb(self, **kwargs):
        username = kwargs["username"]
        result = kwargs["result"]
        gamer = kwargs["gamer"]
        bot = kwargs["bot"]

        if gamer > 2 or gamer < 0:
            return APIError("Incorrect gamer value").json
        if bot > 2 or bot < 0:
            return APIError("Incorrect bot value").json
        if result > 2 or result < 0:
            return APIError("Incorrect result value").json

        sql = f"INSERT INTO games VALUES ('{username}', {gamer}, {bot}, {result})"
        cur = conn.cursor()
        cur.execute(sql)
        return {"ok": True}


japi = jDan734api()


@app.route("/api")
def getapi():
    for arg in arguments:
        params[arg[0]] = request.args.get(*arg)

    if params["action"] is None:
        return page("api.html")
    else:
        return jsonify(japi.__getattribute__(params["action"])(**params))
