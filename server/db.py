from sqlfocus import SQLTable, SQLTableBase
import aiosqlite
import asyncio
import sys

sys.path.append('../')
from config import DB_PATH


async def connect_db():
    return await aiosqlite.connect(DB_PATH)


conn = asyncio.run(connect_db())


class Events(SQLTableBase):
    async def get_unique_users(self):
        users = []

        e = await self.select()

        for user in e:
            if user[1] in users:
                pass
            else:
                users.append(user[1])

        return users


events = Events(conn)
warns = SQLTable("warns", conn)
notes = SQLTable("notes", conn)
pidorstats = SQLTable("pidorstats", conn)


async def init_db():
    await events.create(exists=True, schema=(
        ("chatid", "INTEGER"),
        ("id", "INTEGER"),
        ("name", "TEXT")
    ))

    await warns.create(exists=True, schema=(
        ("user_id", "INTEGER"),
        ("admin_id", "INTEGER"),
        ("chat_id", "INTEGER"),
        ("timestamp", "INTEGER"),
        ("reason", "TEXT")
    ))

    await notes.create(exists=True, schema=(
        ("chatid", "INTEGER"),
        ("name", "TEXT"),
        ("content", "TEXT")
    ))

    await pidorstats.create(exists=True, schema=(
        ("chat_id", "INTEGER"),
        ("user_id", "INTEGER"),
        ("username", "TEXT"),
        ("count", "INTEGER")
    ))

asyncio.run(init_db())
