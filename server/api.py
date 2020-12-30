from server.server import app, page
from flask import request, jsonify
from random import randint


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


japi = jDan734api()


@app.route("/api")
def getapi():
    params = {
        "action": request.args.get("action", type=str),
        "limit": request.args.get("limit", type=int),
        "format": request.args.get("format", type=str)
    }

    if params["action"] is None:
        return page("api.html")
    else:
        return jsonify(japi.__getattribute__(params["action"])(**params))
