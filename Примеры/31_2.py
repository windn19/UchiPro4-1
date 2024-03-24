from flask import Flask

app = Flask(__name__)


def index():
    pass


app.add_url_rule('/', 'index', index)
# или app.add_url_rule('/', view_func=index)
