from flask import Flask, render_template
from werkzeug.contrib.cache import SimpleCache
import json
from flask_socketio import SocketIO, join_room, emit


def create_app():
    app = Flask(__name__)
    store = SimpleCache()
    app.secret_key = 'fdAd3$3#55g^yh6'
    socketio = SocketIO(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/sign_in')
    def sign_in():
        return render_template('registration.html')

    @app.route('/single_game')
    def singlegame():
        return render_template('single_game.html')

    @app.route("/dialog/<int:dialog_id>", methods=['POST'])
    def dialog(dialog_id):
        with open(
            "webapp/dialogs.json", "r"
        ) as dialogs_file:
            dialogs = json.load(dialogs_file)
        dialog = [
            dialog for dialog in dialogs if dialog['id'] == dialog_id][0]
        return render_template('dialog.jinja2', dialog=dialog)

    @app.route("/dialog_multiplayer", methods=['GET'])
    def dialog_multiplayer():
        return render_template(
            'dialog_multiplayer.jinja2',
            async_mode=socketio.async_mode
        )

    @socketio.on('start_dialog', namespace='/test')
    def start_dialog(message):
        dialog_id = 1
        with open(
            "webapp/dialogs_multiplayer.json",
            "r", encoding="utf-8"
        ) as dialogs_file:
            dialogs = json.load(dialogs_file)["dialogs"]
        dialog = [
            dialog for dialog in dialogs if dialog['id'] == dialog_id][0]

        store.set('selected', {
            1: False,
            2: False,
            3: False
        })
        emit('dialog', dialog)

    @socketio.on('selected', namespace='/test')
    def selected_jump(message):
        print(message)
        store.set('selected_jump', message['jump'])
        selected = store.get('selected')
        selected[message['character']] = True
        store.set('selected', selected)
        emit('selected', store.get('selected'))

    @socketio.on('continue', namespace='/test')
    def selected_continue(message):
        selected = store.get('selected')
        selected[message['character']] = True
        store.set('selected', selected)

        if selected[1] and selected[2] and selected[3]:
            dialog_id = store.get('selected_jump')
            with open(
                "webapp/dialogs_multiplayer.json",
                "r", encoding="utf-8"
            ) as dialogs_file:
                dialogs = json.load(dialogs_file)["dialogs"]
            dialog = [
                dialog for dialog in dialogs if dialog['id'] == dialog_id][0]
            store.set('selected', {
                1: False,
                2: False,
                3: False
            })
            emit('dialog', dialog)

    return app
