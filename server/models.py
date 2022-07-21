from pydantic import BaseModel


class Link(BaseModel):
    name: str
    href: str


class Class(BaseModel):
    n: int

    time_start: str
    time_end: str

    method: str

    # lesson_info
    discipline: str
    professor: str
    cabinet: str

    topic: str

    source: Link = None
    task: Link = None


class Day(BaseModel):
    name: str
    date: str

    classes: list[Class]


class Week(BaseModel):
    i: int

    course: str
    days: list[Day]
