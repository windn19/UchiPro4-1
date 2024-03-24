import random

from flask import Flask

app = Flask(__name__)


def get_data():
    data = []
    with open('quotes.txt', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip())
    return data


@app.route("/")
@app.route("/random")
def get_quote():
    data = get_data()
    return random.choice(data)


if __name__ == '__main__':
    app.run(debug=True)
