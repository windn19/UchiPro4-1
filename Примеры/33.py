from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
            <!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8">
                <title>Моя HTML страница</title>
              </head>
              <body>
                <h1>Привет, мир!</h1>
                <p>Я создал эту страницу с помощью Flask.</p>
              </body>
            </html>
            '''
