from flask import Flask

app = Flask(__name__)


@app.route('/user/<name>')
def index(name):
    return '''<h1>Hello,kitty {}</h1>'''.format(name)


if __name__ == '__main__':
    app.run(port=5010)
