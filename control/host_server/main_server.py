from flask import Flask # type: ignore
from flask import Flask, render_template # type: ignore

app = Flask(__name__)


@app.route('/')
def main_server():
    return render_template('index.html')