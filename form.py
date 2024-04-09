from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG', 'JPG', 'JPEG', 'GIF']

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(100), nullable=False)

# db.create_all()  # Ensure the database and tables are created

class InfoForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    photo = FileField('Upload Photo', validators=[
        FileRequired(),
        FileAllowed(app.config['ALLOWED_IMAGE_EXTENSIONS'], 'Images only!')
    ])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = InfoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        new_filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], new_filename)
        form.photo.data.save(filepath)

        # Construct relative path for image to store in DB
        relative_path = os.path.join('static', 'uploads', new_filename)

        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, image_file=relative_path)
        db.session.add(user)
        try:
            db.session.commit()
            return redirect(url_for('success'))
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Database error occurred.", "message": str(e)}), 500

    return render_template('form.html', form=form)

@app.route('/success')
def success():
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
