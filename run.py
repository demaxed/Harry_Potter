from flask_socketio import SocketIO
from webapp import create_app

flask_app = create_app()
socketio = SocketIO(flask_app)
socketio.run(flask_app)
