from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
   return "Главная страница"


@app.route("/news")
def news():
   return "Страница с новостями"


@app.route("/about")
def about():
   return "Сайт с новостями"


if __name__ == '__main__':
   app.run(debug=True)