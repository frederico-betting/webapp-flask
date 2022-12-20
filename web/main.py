from flask import Flask, url_for
from flask_socketio import SocketIO, emit
from web import web_app
from api_v1 import api_v1

# Flask init
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SERVER_NAME'] ='127.0.0.1:14102'
app.config['SECRET_KEY'] = 'secret!'

with app.app_context():
    url_for('static', filename='*.js*')

app.register_blueprint(web_app)
app.register_blueprint(api_v1)

# SocketIO init
socketio_ref = SocketIO(app)
# socketio_ref = SocketIO(app, logger=True, engineio_logger=True)
# This import MUST be after SockerIO is created otherwise it will cause failures.
import socket_comm

if __name__ == '__main__':
    socketio_ref.run(app=app, port=14102)
