from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/login/", methods=['POST'])
    def login():
        return render_template('login.html', email=request.form.get('email'), password=request.form.get('pass'))

    @app.route("/dialog/<int:dialog_id>", methods=['POST'])
    def dialog(dialog_id):
        with open("dialogs.json", "r", encoding="utf-8") as dialogs_file:
            dialogs = json.load(dialogs_file)
        dialog = [ dialog for dialog in dialogs if dialog['id'] == dialog_id ][0]

        # return redirect(url_for("dialog1"))
        return render_template('dialog.jinja2', dialog=dialog)

    return app
