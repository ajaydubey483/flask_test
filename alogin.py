from alogin import Flask, render_template, request
app = Flask(__name__)


@app.route('/loginpage')
def home():
    str=['Input UserName , Input Password , Click On BTN']
    return render_template('index.html',login=str)   #  here we do jinja2 render template


@app.route('/login/<str>',methods = ['GET'])
def login_page(str):
    return str +'Login , Page'


@app.route('/home/<str>',methods = ['POST','GET','PUT'])
def home_page():
    if request.method=="GET":
        return str +'Home , Page'


if __name__=="__main__":
    app.run(debug=True)