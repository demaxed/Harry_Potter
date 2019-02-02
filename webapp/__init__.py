from flask import Flask, render_template
import json


def create_app():
    app = Flask(__name__)
    app.secret_key = 'fdAd3$3#55g^yh6'

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
        dialog = [ dialog for dialog in dialogs if dialog['id'] == dialog_id ][0]
        return render_template('dialog.jinja2', dialog=dialog)

    @app.route('/multiplayer')
    def multiplayer():
        return render_template('')

    return app
