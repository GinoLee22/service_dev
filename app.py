# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '姐姐当我问你如果没遇到我，你是怎么打算哒之后，我就决定我一定要跟你走下去了。希望你可以比我先死哈哈哈哈，我可以送你一程LOL'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
