import sys

sys.path.append('../')
from app import app


def page(file_name):
    with open(f"html/{file_name}", encoding="utf-8") as file:
        return file.read()
