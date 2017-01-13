from flask import Flask, request, render_template, session, flash, redirect, url_for, g
import sqlite3

#H vasi tou project
DATABASE='Project.db'

app = Flask("Project App")
app.config.from_object(__name__)
app.secret_key = 'EnterArch'

#syndesi me db
def connect_database():
    return sqlite3.connect(app.config['DATABASE'])

#homepage                           
@app.route('/')
def homepage():
    return render_template('layout.html')

#syndesi me db
def get_db():
    db = getattr(g, 'Project', None)
    if db is None:
        db = g._Project = sqlite3.connect(DATABASE)
    return db

#login, prwti if leitourgei ws check
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Wrong Credentials, try again'
        else: ##periptwsi swstou login
            session['logged_in'] = True
            flash('You are now logged in!')
            return redirect(url_for('form'))
    return render_template('login.html', error=error)

#logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Goodbye!')
    return redirect(url_for('homepage'))


@app.route('/data')
def form():
    db = get_db()
    cur = db.execute('SELECT Fullname, Surname, Email, Telephone, Age from Customs')
    entries = cur.fetchall()
    return render_template('form.html', entries=entries)

@app.route('/add', methods=['GET','POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.executemany("INSERT INTO Customs (Fullname, Surname) values ([request.form.get('Fullname', 'Surname')])  )")
     ## spasmeno se dyo giati alliws error              
    db.executemany("INSERT INTO Customs (Email, Telephone, Age) values ([request.form.getlist('Email', 'Telephone', 'Age')]))")               
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('form'))
##debugger
if __name__=="__main__":
    app.run(debug=True)
