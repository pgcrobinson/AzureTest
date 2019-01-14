from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Anish, how are you?'


if __name__ =='__main__':
    app.run()
