from .server import app, page, template
from sanic.response import json

from random import randint


arguments = {
    "action": str,
    "limit": int,
    "format": str,
    "username": str,
    "gamer": int,
    "bot": int,
    "result": int
}


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

    def testDB(self):
        return {
            "status": conn.status
        }

    def showDB(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM games;")
        e = cur.fetchall()
        return e

    def addToDB(self):
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
        conn.cursor().execute(sql)
        return {"ok": True}


japi = jDan734api()


@app.route("/api")
@template("api.html")
async def getApi(response):
    params = {}

    for arg in arguments:
        value = response.args.get(arg)

        if value is not None:
            try:
                params[arg] = arguments[arg](value)
            except (TypeError, ValueError):
                params[arg] = None
        else:
            params[arg] = None


    if params.get("action") is None:
        return {
            "status": "dev"
        }

    elif params["action"][0] == "_":
        return json({"error": "actions can't starts with _"})

    try:
        japi._prepare(**params)
        return json(japi.__getattribute__(params["action"])())
    except AttributeError as e:
        print(e)
        return json({
            "error": "action {} not found".format(params["action"])
        })
