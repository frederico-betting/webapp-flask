"""Rock-Paper-Scissors game."""
import signal
import sys
import socketio
import threading

sio = socketio.Client()

def main() -> None:
    """Start point."""
    t = threading.Thread(target=user_input)
    t.start()
    sio.connect('http://localhost:14102')
    sio.wait()

@sio.event
def user_input():
    while True:
        input_value = input(
            'Please, type a message: '
        )
        sio.emit('my response', {'response': input_value})

# pylint: disable=redefined-outer-name,unused-argument
def signal_handler(signal: signal.Signals, frame: any) -> None:
    """Handle any signal received."""
    print('\nBye!')
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
