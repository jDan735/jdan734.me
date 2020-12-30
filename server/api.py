from server.server import app, page
from flask import request, jsonify
from random import randint


@app.route("/api")
def api():
    action = request.args.get("action", type=str)
    limit = request.args.get("limit", type=int)
    format_ = request.args.get("format", type=str)

    if action is None:
        return page("api.html")
    else:
        if action == "ban":
            return jsonify({"ban": True, "date": "always has been"})
        elif action == "random":
            if limit is None:
                limit = 10
            elif limit >= 10000:
                return jsonify({"error": "big limit"})

            return jsonify({"number": randint(0, limit)})
