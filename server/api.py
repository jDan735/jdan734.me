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

    def _prepare(self, **kwargs):
        for arg in kwargs:
            self.__dict__[arg] = kwargs[arg]

    def ban(self):
        return {"ban": True, "date": "always has been"}

    def random(self):
        limit = 10 if self.limit is None else self.limit

        if limit > 10000:
            return APIError("Limit is bigger is 10000").json

        return {"number": randint(0, limit)}

    def testdb(self):
        return {
            "status": conn.status
        }

    def showdb(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM games;")
        e = cur.fetchall()
        return e

    def addtodb(self):
        if self.gamer > 2 or self.gamer < 0:
            return APIError("Incorrect gamer value").json
        if self.bot > 2 or self.bot < 0:
            return APIError("Incorrect bot value").json
        if self.result > 2 or self.result < 0:
            return APIError("Incorrect result value").json

        sql = "INSERT INTO games VALUES ({username}, {gamer}, {bot}, {result})"
        sql = sql.format(username=self.username,
                         gamer=self.gamer,
                         bot=self.bot,
                         result=self.result)
        cur = conn.cursor()
        cur.execute(sql)
        return {"ok": True}


japi = jDan734api()


@app.route("/api")
def getApi():
    for arg in arguments:
        params[arg[0]] = request.args.get(arg[0], type=arg[1])

    if params["action"] is None:
        return page("api.html")
    elif params["action"][0] == "_":
        return jsonify({"error": "actions can't starts with _"})
    else:
        try:
            japi._prepare(**params)
            return jsonify(japi.__getattribute__(params["action"])())
        except AttributeError:
            return jsonify({
                "error": "action {} not found".format(params["action"])
            })
