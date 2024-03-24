from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Главная страница'


@app.route('/news')
def news():
    return 'Новости'


@app.route('/news_detail/1')
def news_detail1():
    return 'Новость 1'


@app.route('/news_detail/2')
def news_detail2():
    return 'Новость 2'
