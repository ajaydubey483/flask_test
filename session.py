from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/set_session')
def set_session():
    if 'username' in session:
        session['username'] = 'Ajay'
        return 'Session set successfully'


@app.route('/get-session')
def get_session():
    username = session.get('username')
    if username:
        return f'Username: {username}'
    else:
        return 'No username found in session'
    

@app.route('/delete-session')
def delete_session():
    if 'username' in session:
        session.pop('username')
        return 'Username deleted from session'
    else:
        return 'No username found in session'    
    

@app.route('/delete-all-sessions')
def delete_all_sessions():
    session.clear()
    return 'All sessions deleted'  

if __name__=="__main__":
   app.run(debug=True)  