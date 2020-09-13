from flask import Flask
from wikipedia import Wikipedia
app = Flask(__name__)


@app.route('/')
def index():
    with open("index.html", encoding="utf-8") as index:
        return index.read()


@app.route('/a')
def a():
    with open("a.html", encoding="utf-8") as af:
        return af.read()


@app.route('/obama')
def sosat():
    return "sosat"


@app.route('/wiki/<page_name>')
def wiki(page_name):
    wiki = Wikipedia("ru")
    search = wiki.search(page_name)
    if search == -1:
        with open("404.html", encoding="utf-8") as index:
            return index.read()

    head = '<link rel="icon" type="image/png" href="/static/favicon-16x16.png" sizes="16x16" /><link rel="icon" type="image/png" href="/static/favicon-32x32.png" sizes="32x32" /><link rel="icon" type="image/png" href="/static/favicon-96x96.png" sizes="96x96" /><link rel="stylesheet" href="/static/css/style.css?v=1.4.1" /><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />'
    style = '<link rel="stylesheet" href="/static/css/style.css?v=1.4.0"/>'
    h1 = f'<h1>{search[0][0]}</h1>'

    image_url = wiki.getImageByPageName(search[0][0], 400)

    if image_url == -1:
        img = ""
    else:
        full_image_url = wiki.getImageByPageName(search[0][0], 400)
        img = f'<a href="{full_image_url}"><img class="wiki_photo" src="{image_url}"></a>'

    result = head + style + h1 + img + str(wiki.getPage(search[0][0], -1))

    return result


@app.errorhandler(404)
def not_found(error):
    with open("404.html", encoding="utf-8") as index:
        return index.read()


@app.errorhandler(505)
def not_found_shizha(error):
    return "Не сюда)"


@app.route('/lorem')
def lorem():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ac consequat ex. Phasellus enim urna, fermentum at lacus sit amet, rhoncus pulvinar diam. Suspendisse vestibulum accumsan volutpat. Etiam at nulla est. Nam aliquet, nibh in sodales ornare, ante orci maximus justo, non scelerisque quam elit at justo. Nulla imperdiet, est in eleifend ultrices, nibh sapien fermentum dolor, vitae tincidunt nunc tellus vitae nulla. Duis gravida consequat nisi, placerat varius ipsum. Proin quis tortor dui. Quisque eros ante, pellentesque et dignissim nec, rhoncus vitae ligula. Maecenas eleifend lacus eget aliquet mattis. Praesent aliquam dictum dolor id luctus. Ut fringilla dui vitae mi laoreet semper.<br><br>Donec diam risus, interdum pellentesque dictum vitae, ullamcorper quis velit. Nulla facilisi. In hac habitasse platea dictumst. In sodales ex at lorem venenatis sodales. Cras eu imperdiet nunc. Fusce molestie dictum semper. Proin eget nisl vel neque venenatis ultrices. Pellentesque id erat metus. Vivamus ante orci, malesuada a pellentesque nec, fermentum sed lacus.<br><br>Donec efficitur dolor lacus, eget consequat augue placerat vitae. Curabitur vel turpis et mauris placerat consectetur eget at magna. Curabitur sagittis, metus vel vehicula bibendum, nulla quam viverra est, id dictum ipsum elit lacinia turpis. Donec placerat sed massa eu pretium. Proin non massa nibh. Maecenas maximus venenatis justo, quis lobortis tellus. Etiam auctor, ex a porttitor hendrerit, tortor ligula volutpat dui, ac malesuada purus magna ut lacus.<br><br>Praesent vulputate iaculis odio, vel convallis massa ultricies in. Nullam vulputate, nibh ut faucibus congue, justo turpis finibus mi, at ornare erat augue eget massa. Nunc ut semper massa. Praesent rutrum nibh vel velit aliquam dignissim. Donec sed risus sollicitudin, placerat sem ut, commodo leo. Cras in hendrerit arcu. Etiam eget finibus nulla. Curabitur sit amet lacinia mauris. Etiam et metus at dolor aliquam dapibus. Nulla facilisi. Sed et elit quis orci tempus consequat. Praesent finibus efficitur orci. Integer nibh augue, laoreet et magna non, tempus malesuada justo. In et auctor urna.<br><br>Praesent leo est, laoreet vitae orci eget, tempor vehicula erat. Pellentesque ultrices lectus non dolor pellentesque, ac pharetra risus cursus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec bibendum vulputate nibh fermentum mollis. Maecenas in fermentum neque. Suspendisse aliquam ornare nisl eget sollicitudin. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut ultrices ipsum mi, eu sagittis justo mollis bibendum. Phasellus ac lobortis ex, vitae lobortis eros. Nullam hendrerit leo at leo tincidunt euismod. "


if __name__ == '__main__':
    app.run(port=5050)
