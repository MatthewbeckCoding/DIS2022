from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, widgets, SelectField, HiddenField, RadioField
from wtforms.fields.html5 import DateField # see https://stackoverflow.com/questions/26057710/datepickerwidget-with-flask-flask-admin-and-wtforms
from wtforms.validators import DataRequired, URL, Optional, ValidationError, Length, Email, EqualTo #need to install email validator separately
import random  # needed for random number generation
import sqlite3
import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = "myverysecretkey"
#connect to the database
con = sqlite3.connect("signup.db", check_same_thread=False)
con.row_factory = sqlite3.Row
#create a cursor/pointer to navigate the database
cur = con.cursor()
#create the forms for use
class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    sex = SelectField('Sex', choices=['m','f'] )
    earns = StringField('Earns', validators=[DataRequired()])
    likes = StringField('Likes', validators=[DataRequired()])
    dislikes = StringField('Dislikes', validators=[DataRequired()])
    submit = SubmitField('Submit')

#create the routes
@app.route("/", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            age = form.age.data
            sex = form.sex.data
            earns = form.earns.data
            likes = form.likes.data
            dislikes = form.dislikes.data

            sql = """
                    insert
                    into people (name, age, sex, earns, likes, dislikes)
                    values (?, ?, ?, ?, ?, ?)"""

            try:
                cur.execute(sql,(name, age, sex, earns, likes, dislikes))
                con.commit()
            except:
                flash("Oops! Something went wrong")
            else:
                flash("Account registered and logged it")
                session['name'] = name
                session['age'] = age
                session['sex'] = sex
                session['earns'] = earns
                session['likes'] = likes
                session['dislikes'] = dislikes
                return redirect(url_for('index'))

    return render_template("register.html", form=form)

#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)