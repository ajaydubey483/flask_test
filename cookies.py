from flask import Flask,render_template,request
app=Flask(__name__)



@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':   
    # resp = make_response(render_template('readcookie.html'))
    # resp.set_cookie('userID', user)
    return 'cokkies has been seted successfully'
   

@app.route('/getcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'GET':   
    # name = request.cookies.get('userID')
    return 'cokkies has been geted successfully'