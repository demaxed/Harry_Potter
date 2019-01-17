from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json


my_flask_app = Flask(__name__)

@my_flask_app.route("/")
def index():
    return render_template('index.html')

@my_flask_app.route("/login/", methods=['POST'])
def login():
    return render_template('login.html', email=request.form.get('email'), password=request.form.get('pass'))

@my_flask_app.route("/dialog/<int:dialog_id>", methods=['POST'])
def dialog(dialog_id):
    with open("dialogs.json", "r", encoding="utf-8") as dialogs_file:
        dialogs = json.load(dialogs_file)
    dialog = [ dialog for dialog in dialogs if dialog['id'] == dialog_id ][0]

    # return redirect(url_for("dialog1"))
    return render_template('dialog.jinja2', dialog=dialog)

# @my_flask_app.route('/dialog1/')
# def dialog1():
#     return render_template('dialog1.html')

if __name__=="__main__":
    my_flask_app.run(debug=True)
    