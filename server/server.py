import sys
sys.path.append('../')

from app import app


def page(file_name):
    with open(file_name, encoding="utf-8") as file:
        return file.read()


pages = {
    "index": page("index.html"),
    "kanobu": page("kanobu.html"),
    "timer": page("timer.html"),
    "404": page("404.html"),
    "lorem": page("lorem.html"),
    "test": page("test.html"),
    "ligatures": page("ligatures.html")
}
