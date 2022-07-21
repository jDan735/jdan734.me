from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from .server import app
import httpx

from bs4 import BeautifulSoup

from .models import Week, Day, Class, Link


@app.get("/pavel", response_class=HTMLResponse)
async def index(request: Request):
    import pprint

    pavel, table = get_pavel(week=122)

    # for day in pavel.days:
    #     print(day.name)
    #     print("==========\n")
    #     for class_ in day.classes:
    #         print(class_.n)
    #         print(class_.discipline)
    #         print(class_.professor)
    #         print(class_.topic)
    #         print("---------")

    import json
    out = json.dumps(json.loads(pavel.json()), indent=4, ensure_ascii=False)

    with open("122_week.json", "w") as file:
        file.write(out)

    return "<pre>" + str(out) + "</pre><br\>" + str(table)


def get_pavel(mn: int = 2, obj: int = 21, week: int = 121) -> Week:
    site = httpx.get(f"https://lk.ks.psuti.ru/?mn={mn}&obj={obj}&wk={week}")
    soup = BeautifulSoup(site.text, "lxml")

    table = soup.find_all("table")[4]

    for tag in table.find_all("tr"):
        if tag.td.text == "":
            tag.replace_with("")

    for tag in table.find_all("tr"):
        if tag.td.text == "№ пары":
            tag.replace_with("")

    for tag in table.find_all("br"):
        tag.replace_with("\n")

    # [
    #     {
    #         lesson,
    #         lessons_list
    #     }
    # ]

    days = []

    for tr in table.find_all("tr")[1:]:
        try:
            is_lesson = tr.attrs["align"] == "center"
        except KeyError:
            is_lesson = False

        if not is_lesson:
            days.append(dict(source=tr, classes=[]))
        else:
            days[-1]["classes"].append(tr)

    days = list(filter(lambda x: len(x["classes"]) > 0, days))
    print(len(days))

    week = Week(
        i=int(table.find_all("tr")[1]
                .h3.text.strip().split("/")[1]
                .strip().split(" ")[0]),
        course=table.find_all("tr")[0].text.strip(),

        days=[Day(
            name=day["source"].h3.text.split("/")[0].split(" ")[0],
            date=day["source"].h3.text.split("/")[0].split(" ")[1],
            classes=[Class(
                n=class_.find_all("td")[0].text,

                time_start=class_.find_all("td")[1].text.split(" – ")[0].strip(),
                time_end=class_.find_all("td")[1].text.split(" – ")[1].strip(),

                method=class_.find_all("td")[2].text,

                discipline=(lesson_info := class_.find_all("td")[3].text.strip().split("\n"))[0],
                professor=lesson_info[1],
                cabinet=lesson_info[2].split(" ")[1] if len(lesson_info) > 2 else "None",

                topic=class_.find_all("td")[4].text.strip(),

                source=Link(
                    name=source.text.strip(),
                    href=source.a["href"]
                ) if (source := class_.find_all("td")[5]).text.strip() != "" else None,
                task=Link(
                    name=source.text.strip(),
                    href=source.a["href"]
                ) if (source := class_.find_all("td")[6]).text.strip() != "" else None,
            ) for class_ in day["classes"]]
        ) for day in days]
    )

    return Week.parse_obj(week)
