import json

with open("result.json", encoding="utf-8") as file:
    data = json.loads(file.read())
    for message in data["messages"]:
        name = "Электрическая Говноварка"
        try:
            if message["from_id"] == 1098195500:
                try:
                    print(f'{message["id"]} <{name}> {message["poll"]["question"]}')
                    print()

                    for answer in message["poll"]["answers"]:
                        padding = len(str(message["id"]) + f" [{name}]") * " "
                        print(f'{padding} [{answer["text"]}] {answer["voters"]}')

                    print()
                except:
                    padding = (len(str(message["id"]) + f" [{name}]") + 1) * " "
                    text = message["text"].replace("\n", "\n" + padding)
                    print(f'{message["id"]} <{name}> {text}')
        except:
            pass

# with open("result.json", encoding="utf-8") as file:
#     data = json.loads(file.read())
#     for message in data["messages"]:
#         try:
#             print(f'{message["id"]} [{message["from"]}] {message["poll"]["question"]}')
#             for answer in message["poll"]["answers"]:
#                 print(f'{len(str(message["id"])) * " "} < {answer["text"]} > {answer["voters"]}')
#             print()
#         except Exception as e:
#             pass
