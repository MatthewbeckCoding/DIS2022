from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_login import login_required, current_user
from datetime import datetime, date
from flask_wtf import FlaskForm
import sqlite3
import datetime
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectMultipleField, SelectField, widgets
from wtforms.fields.html5 import \
    DateField
from wtforms.validators import DataRequired, URL, Optional, InputRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ddksididkdkdl'
con = sqlite3.connect("catalogue.db", check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()

app.config['UPLOADED_IMAGES_DEST'] = 'static/images/acts'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class TopicForm(FlaskForm):
    topic_name = StringField('Topic Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SubmitVideo(FlaskForm):
    url = StringField('URL', validators=[DataRequired(message="You must submit a URL"), URL(message="Nota valid URL")])
    video_description = TextAreaField('Description', validators=[DataRequired()])
    topics = MultiCheckboxField('Topics for this video', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit URL')

class SubmitReview(FlaskForm):
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            un = form.username.data
            pw = form.password.data

            sql = """
                    select *
                    from users
                    where username = ?
                    and password = ?;
            """
            cur.execute(sql, (un, pw))
            result = cur.fetchall()
            if len(result) == 1:
                session['username'] = result[0][1]
                session['firstname'] = result[ 0][2]
                session['surname'] = result[0][3]
                session['is_teacher'] = result[0][4]
                if session['is_teacher']:
                    session['teacher_code'] = result[0][5]
                return redirect(url_for('home'))
            else:
                flash("INCORRECT")
        else:
            flash("something missing")
    return render_template('login.html', title='Login', form=form)

@app.route('/home')
def home():
    if session['username']:
        print(type(session['username']))
        sql = """select *
                from videos
                where video_id in (
                    select video_id
                    from topic_videos
                    where topic_id in (
                        select topic_id
                        from topics
                        where subject_code in (
                            select subject_code
                            from users u, enrolments e, classes c
                            where u.username = e.username
                            and e.class_id = c.class_id
                            and u.username = ?)))
                            and is_approved = 'True'
                            order by date_submitted desc
                            limit 3;
                """
        cur.execute(sql, (session['username'],))
        home_results = cur.fetchall()

        sql = """select *
                        from videos
                        where submitted_by = ?
                        and is_approved = 'True'
                        order by date_submitted asc
                        limit 3;"""
        
        cur.execute(sql, (session['username'],))
        your_results = cur.fetchall()
        return render_template("home.html", title="home", home_results=home_results, your_results=your_results)
    else:
        return redirect('login')


@app.route('/logout')
def logout():
    session['username'] = None
    session['firstname'] = None
    session['surname'] = None
    session['is_teacher'] = None
    session['teacher_code'] = None

    flash("You have successfully logged out")
    return redirect(url_for('login'))

@app.route('/subjects', methods=['GET'])
def subjects():
    if session['username']:
        if request.args.get('sid'):
            id = request.args.get('sid')
            sql = """
                    select subject_code
                    from enrolments e, classes c
                    where e.class_id = c.class_id
                    and username = ? ;"""
            cur.execute(sql, (id,))
            results = cur.fetchall()

            return render_template("subjects.html", title="Subjects", student_subjects=results)
    else:
        return redirect('login')

@app.route('/subject_topics', methods=['GET'])
def subject_topics():
    if session['username']:
        if request.args.get('ssid'):
            id = request.args.get('ssid')
            sql = """
                    select subject_code
                    from classes c, users u, enrolments e
                    where u.username = e.username
                    and e.class_id = c.class_id
                    and subject_code = ?;"""

            cur.execute(sql, (id,))
            thesubject_results = cur.fetchone()
            session['subject_code'] = thesubject_results[0]

            sql = """
                            select topic_name
                            from topics
                            where subject_code = ?;"""
            cur.execute(sql, (id,))
            topic_results = cur.fetchall()

            return render_template("subject_topics.html", title="Subject Topics", thesubject_results=thesubject_results,
                                   topic_results=topic_results)

@app.route('/topicsform', methods=['GET', 'POST'])
def topicsform():
    if session['username']:
        form = TopicForm()
        username = session['username']
        subject_code = session['subject_code']
        if request.method == 'POST':
            if form.validate_on_submit():
                topic_name = form.topic_name.data
                sql = """
                        insert
                        into topics (topic_name, username, subject_code)
                        values (?, ?, ?)"""
                try:
                    cur.execute(sql, (topic_name, username, subject_code))
                    con.commit()
                except:
                    flash('Something went wrong')
                else:
                    flash("topic created")
                    session['topic_name'] = topic_name
                    session['username'] = username
                    session['subject_code'] = subject_code
                    return redirect(url_for('home'))

        return render_template('topicsform.html', title='Topics Form', form=form)

@app.route('/videos', methods=['GET'])
def videos():
    if session['username']:
        if request.args.get('tid'):
            id = request.args.get('tid')

            sql = """
                    select *
                    from topics
                    where topic_name = ?;"""
            cur.execute(sql, (id,))
            thetopic_results = cur.fetchone()

            sql = """
                    select *
                    from videos v, topic_videos tv, topics t
                    where v.video_id = tv.video_id
                    and tv.topic_id = t.topic_id
                    and topic_name = ?;"""

            cur.execute(sql, (id,))
            video_results = cur.fetchall()
            return render_template("videos.html", title="Videos", thetopic_results=thetopic_results, video_results=video_results)

@app.route('/videoform', methods=['GET', 'POST'])
def videoform():
    if session['username']:
        form = SubmitVideo()
        my_topics = []
        sql = """
        select topic_id, topic_name, s.subject_code
        from topics t, subjects s, enrolments e, users u, classes c
        where t.subject_code = s.subject_code
        and s.subject_code = c.subject_code
        and c.class_id = e.class_id
        and e.username = u.username
        and u.username = ?
        order by s.subject_code asc, topic_id asc;"""
        cur.execute(sql, (session['username'],))
        results = cur.fetchall()
        for row in results:
            my_topics.append((row['topic_id'], row['subject_code'] + ' - ' + row['topic_name']))
        form.topics.choices = my_topics
        if request.method == 'POST':
            if form.validate_on_submit():
                full_url = form.url.data
                url = full_url[-11:]
                video_description = form.video_description.data
                video_topics = []
                date_submitted = datetime.datetime.now()
                for v in form.topics.data:
                    video_topics.append(int(v))
                if session['is_teacher'] == 'True':
                    is_approved = 'True'
                else:
                    is_approved = 'False'
                sql_video = """
                            insert
                            into videos(url, video_description, submitted_by, is_approved, date_submitted)
                            values(?, ?, ?, ?,?);"""
                try:
                    cur.execute(sql_video, (url, video_description, session['username'], is_approved, date_submitted))
                    con.commit()
                except:
                    flash('Something went wrong')
                else:
                    video_videoID = cur.lastrowid
                    sql_topics = """
                                    insert
                                    into topic_videos(video_id, topic_id)
                                    values (?, ?);"""
                    try:
                        for topic in video_topics:
                            cur.execute(sql_topics, (video_videoID, topic))
                        con.commit()
                    except:
                        flash('Something went wrong')
                    else:
                        if session['is_teacher'] != 'True':
                            flash('video submitted for review')
                        else:
                            flash('video submitted and approved')
                        return redirect('home')
        return render_template('videoform.html', title='topic form', form=form)

@app.route('/review', methods=['GET', 'POST'])
def review():
    if session['username']:
        if request.args.get('rid'):
            id = request.args.get('rid')

            sql = """
                    select *
                    from videos
                    where video_id in (
                        select video_id
                        from topic_videos
                        where topic_id in (
                            select topic_id
                            from topics
                            where subject_code in (
                                select subject_code
                                from users u, enrolments e, classes c
                                where u.username = e.username
                                and e.class_id = c.class_id
                                and u.username = ?
                                and is_approved = 'False')));"""
            cur.execute(sql, (id,))
            review_results = cur.fetchall()

            for row in review_results:
                if request.method == "POST":
                    video_id = row['video_id']
                    sql = """
                        update videos
                        set is_approved = 'True'
                        where video_id = ?; """
                    cur.execute(sql, (video_id,))
                    con.commit()
                    flash("review complete")
            return render_template("review.html", title="Review", review_results=review_results)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host, port, debug=True)
