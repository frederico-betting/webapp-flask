from flask import Blueprint, render_template, session, abort, url_for

web_app = Blueprint('web_app',__name__)

@web_app.route("/")
def main():
    return "Hello World from webapp!"

@web_app.route('/hi/')
@web_app.route('/hi/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
