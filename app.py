from flask import Flask, render_template, flash, request, url_for, redirect, json, jsonify
from content_sample import Content
from flask_mail import Mail, Message

TOPIC_DICT = Content()


app = Flask(__name__, static_folder='static', static_url_path='')

app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'santiagojosephmario08@gmail.com',
    MAIL_PASSWORD = 'awo22148'
)
mail = Mail(app)

@app.route('/emailhtml')
def send_email_html():
    try:
        msg = Message('Feedback Client', sender='josephmario_santiago@yahoo.com', recipients=['josephmario_santiago@yahoo.com'])
        msg.body = 'Hello'
        mail.send(msg)
        return 'Message Sent!'
    except Exception as e:
        return str(e)



@app.route('/email')
def send_email():
    try:
        msg = Message('Feedback Client', sender='josephmario_santiago@yahoo.com', recipients=['josephmario_santiago@yahoo.com'])
        msg.body = 'Hello '
        mail.send(msg)
        return 'Message Sent!'
    except Exception as e:
        return str(e)

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return jsonify({'status':'OK','user':user,'pass':password});


@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/json')
def json():
    book = {}
    book['tom'] = {
        'name': 'tom',
        'address': '1 red street',
        'phone': 909090
    }
    book['bob'] = {
        'name': 'bob',
        'address': '1 green street',
        'phone': 222222
    }
    json_string = jsonify(book)
    return  json_string

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/vestinit", methods=['GET','POST'])
def vestinit():
    try:
        attempted_username = request.form['username']
        attempted_subject = request.form['subject']
        attempted_email = request.form['email']
        attempted_message = request.form['message']

        # flash(request.method)
        # flash(attempted_username)
        # flash(attempted_subject)
        # flash(attempted_email)
        # flash(attempted_message)

        if attempted_username == "" and attempted_subject == "" and attempted_email == "" and attempted_message == "":
            return "Blank"
        else:
            return redirect(url_for('send_email_html'))

    except Exception as e:
        flash(e)
    return render_template("vestinit.html")


@app.route("/extendsandblock")
def extendsandblock():
    flash("Flash test")
    return render_template('extendsandblock.html', TOPIC_DICT = TOPIC_DICT)

@app.route("/home")
def home():
    return 'This is home page.'

@app.route("/NameList")
def NameList():
    name = ["Joseph", "Jayhson", "Mariel"];
    return render_template("NameList.html", name=name)

@app.route("/MappingMultiple/<name>")
def MappingMultiple(name):
    return render_template("MappingMultiple.html", name=name)

@app.route("/ViewProfile/<name>")
def ViewProfile(name):
    return render_template("ViewProfile.html", name=name)

@app.route("/profile/<username>")
def profile(username):
    return "Hey there %s" % username

@app.route("/client/<int:userid>")
def client(userid):
    return "User Id %s" % userid

@app.errorhandler(404)
def page_not_found(e):
    return("ERROR FOUND!")

@app.route('/login', methods=['GET','POST'])
def login_page():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            flash(attempted_username)
            flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "12345":
                return redirect(url_for('extendsandblock'))
            else:
                error = "Invalid username and password. Try Again"

        return render_template("login.html", error = error)

    except Exception as e:
        flash(e)
    return render_template("login.html", error = error)

if __name__ == "__main__":
    app.secret_key = 'many random bytes'
    app.run(
        debug=True
    )
