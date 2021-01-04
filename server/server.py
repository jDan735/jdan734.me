from os import environ

import psycopg2
import json
import sys

sys.path.append('../')
from app import app


def page(file_name):
    with open(f"html/{file_name}", encoding="utf-8") as file:
        return file.read()


if "DATABASE_URL" in environ:
    con = psycopg2.connect(environ["DATABASE_URL"],
                           sslmode='require')
else:
    with open("dbconf.json") as bdconf_file:
        bdconf = json.loads(bdconf_file.read())
        con = psycopg2.connect(**bdconf)
