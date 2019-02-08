from flask import Flask, render_template
from flask_login import LoginManager
import json

from webapp.db import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    app.register_blueprint(user_blueprint)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/single_game')
    def singlegame():
        return render_template('single_game.html')

    @app.route("/dialog/<int:dialog_id>", methods=['POST'])
    def dialog(dialog_id):
        with open(
            "webapp/dialogs.json",
            "r", encoding="utf-8"
        ) as dialogs_file:
            dialogs = json.load(dialogs_file)["dialogs"]
        dialog = [dialog for dialog in dialogs if dialog['id'] == dialog_id][0]
        return render_template('dialog.jinja2', dialog=dialog)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
