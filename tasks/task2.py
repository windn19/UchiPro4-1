from flask import Flask

app = Flask(__name__)


def get_fibonacci_numbers(n):
    numbers = [1, 1]
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers


def get_fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


@app.route("/fibonacci")
def fibonacci():
    return ' '.join([str(s) for s in get_fibonacci_numbers(n)])


@app.route('/fib')
def fib():
    return '<br>'.join([str(s) for s in get_fib(100)])


if __name__ == '__main__':
    n = 100
    app.run(debug=True)
