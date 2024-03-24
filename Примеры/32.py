from flask import Flask, url_for

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


with app.test_request_context():
    print(url_for('index'))
    print(url_for('news'))
    print(url_for('news_detail', id=1))
