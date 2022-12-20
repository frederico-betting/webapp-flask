from flask_socketio import SocketIO, emit
from __main__ import socketio_ref

@socketio_ref.on('connect')
def handle_connection():
    print('connected')

@socketio_ref.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio_ref.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio_ref.on('my response')
def msg_client(data):
    emit('my response', data, broadcast=True)
