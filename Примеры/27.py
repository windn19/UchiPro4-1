from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Главная страница'


@app.route('/news')
def news():
    return 'Новости'


@app.route('/news_detail/<int:id>')
def news_detail(id):
    return f'Новость {id}'
