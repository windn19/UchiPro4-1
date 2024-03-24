from flask import Flask

app = Flask(__name__)


@app.route('/category/')
def category():
    return 'Категории новостей'


@app.route('/news')
def news():
    return 'Новости'
