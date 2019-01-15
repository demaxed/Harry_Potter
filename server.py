from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
my_flask_app = Flask(__name__)

@my_flask_app.route("/")
def index():
    return render_template('index.html')

@my_flask_app.route("/login/", methods=['POST'])
def login():
    return render_template('login.html', email=request.form.get('email'), password=request.form.get('pass'))

@my_flask_app.route("/dialog/<int:dialog_id>", methods=['POST'])
def dialog(dialog_id):
    dialog = {
        'text': "olololo ggg",
        'jumps': [
            {
                'dialog_id': 50,
                'text': "Нажми сюда, чтобы ололо"
            },
            {
                'dialog_id': 49,
                'text': "Нажми сюда, чтобы гггг"
            }
        ]
    }

    # return redirect(url_for("dialog1"))
    return render_template('dialog.jinja2', dialog=dialog)

# @my_flask_app.route('/dialog1/')
# def dialog1():
#     return render_template('dialog1.html')

if __name__=="__main__":
    my_flask_app.run(debug=True)
    