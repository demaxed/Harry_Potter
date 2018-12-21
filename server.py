from flask import Flask, render_template, request
my_flask_app = Flask(__name__)

@my_flask_app.route("/")
def index():
    return render_template('index.html')

@my_flask_app.route("/login/", methods=['POST'])
def login():
    return render_template('login.html', email=request.form.get('email'), password=request.form.get('pass'))

@my_flask_app.route("/dialog_harry", methods=['POST'])
def dialog_harry():
    return render_template('dialog1.html')

@my_flask_app.route('/dialog1/')
def dialog1():
    return render_template('dialog1.html')

if __name__=="__main__":
    my_flask_app.run(debug=True)
    