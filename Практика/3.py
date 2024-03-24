import requests
from flask import Flask

app = Flask(__name__)


def get_course():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = ''
    print(response['Valute'])
    for _, data in response['Valute'].items():
        result += f'{data["Nominal"]} {data["Name"]} стоит {data["Value"]} руб.<br>'
    return result


@app.route("/money")
def money():
    return get_course()


if __name__ == '__main__':
    app.run(debug=True)
