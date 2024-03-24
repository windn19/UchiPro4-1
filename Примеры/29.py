from flask import Flask

app = Flask(__name__)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    return f'Новость {id}'


@app.route('/category/<string:name>')
def category_detail(name):
    return f'Категория {name}'
