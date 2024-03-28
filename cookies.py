from flask import Flask,render_template,request,make_response
app=Flask(__name__)

@app.route('/setcookie')
def setcookie():
    resp = make_response('<h1>Cookie Set Success!</h1>')
    resp.set_cookie('username', 'Python_Flask')
    return resp

@app.route('/getcookie', methods=['GET'])
def getcookie():
    name = request.cookies.get('username')
    return  '<h1>welcome ' + name + '</h1>'

@app.route('/setexpiringcookie')
def setexpiringcookie():
    resp = make_response(render_template('cookie.html'))
    resp.set_cookie('username', 'Python_Flask', max_age=60*60*24*30) #expires in 30 days
    return resp

@app.route("/delete-cookies")
def delete_cookies():
    response = make_response("Deleted the cookie ")
    response.delete_cookie("_dd_s")
    return response


if __name__=="__main__":
   app.run(debug=True)