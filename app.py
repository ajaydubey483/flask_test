from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/products')
def products():
    return 'This is Products Page'

@app.route('/ajay')
def ajay():
    return 'Hello Dubey Ji'

# app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

