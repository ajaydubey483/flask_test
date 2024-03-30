from flask import Flask, request , render_template
app = Flask(__name__)

submissions = {}


@app.route('/login/page')
def home():
    return render_template('page.html')


@app.route('/submit', methods=['POST'])
def login():
    email = request.form.get('email')
    name  =  request.form.get('name')
    mobile = request.form.get('mobile')
    # Simple validation rules
    if ".com" not in email or not name or not mobile.isdigit() or len(mobile) != 10:
        return "Failed to Submit!"
    
    # Check if this email has already been submitted with the same name and mobile
    if email in submissions and submissions[email]['name'] == name and submissions[email]['mobile'] == mobile:
        return "Error: These details already exist."
    
    # If it's a new and valid submission, store the details
    submissions[email] = {'name': name, 'mobile': mobile}
    return "Details Submitted Successfully."



if __name__ == '__main__':
    app.run(debug=True)