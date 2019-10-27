from flask import Flask

app = Flask(__name__)

#http://127.0.0.1/
@app.route('/')
def index():
    return 'Hello World!'