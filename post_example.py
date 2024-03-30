from flask import Flask, request , render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    uname = request.form.get('uname')
    passwrd = request.form.get('pass')
    if uname == "ayush" and passwrd == "google":
        return "Welcome %s" % uname
    else:
        return "Invalid username or password 401 error", 401  


if __name__ == '__main__':
    app.run(debug=True)