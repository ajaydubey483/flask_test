from flask import Flask, request , render_template, jsonify
import sqlite3


app = Flask(__name__)
submissions = {}

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS students (email TEXT, name TEXT, mobile TEXT)')
        

@app.route('/')
def home():
    return render_template('page.html')



@app.route('/submit', methods=['POST'])
def login():
    email = request.form.get('email')
    name  =  request.form.get('name')
    mobile = request.form.get('mobile')

    # Simple validation rules
    if ".com" not in email or not name or not mobile.isdigit() or len(mobile) != 10:
        return "Error: Failed to Submit!"
    
    # Check if this email has already been submitted with the same name and mobile
    if email in submissions and submissions[email]['name'] == name and submissions[email]['mobile'] == mobile:
        return "Error: These details already exist."
    
    
    with sqlite3.connect("database.db") as con:  # Fixed the syntax error here
        cur = con.cursor()
        cur.execute("INSERT INTO students (email, name, mobile) VALUES (?, ?, ?)", (email, name, mobile))
        con.commit()
        msg = "Record successfully added"

    # If it's a new and valid submission, store the details
    submissions[email] = {'name': name, 'mobile': mobile}
    return "Details Submitted Successfully."


@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    # cur.execute("DELETE FROM students")
   
    rows = cur.fetchall()
    return render_template("list.html", rows=rows)



if __name__ == '__main__':
    app.run(debug=True, port=80)


    

