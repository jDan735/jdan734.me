from flask import Flask

app = Flask(__name__, static_url_path="/")

from ftp import *
from server import *


if __name__ == '__main__':
    app.run(port=5050)
