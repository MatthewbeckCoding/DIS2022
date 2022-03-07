from flask import Flask, render_template, request, redirect, flash, url_for, session
app = Flask(__name__)

#########################################################################
# HTTP Routes
#########################################################################
@app.route('/')
def home():
    if request.args:
        #return request.args
        if request.args.get('lang') != 'en':
            return 'sorry not english'
    else:
        return 'this is in eglish'
@app.route('/about')
def index():
    return 'You have found the about page route'

@app.route('/contact')
def contact():
    if request.args:
        #return request.args
        if request.args.get('source') == 'facebook':
            return 'message'
    else:
        return 'THis da contact page hit me up email'

@app.route('/menus')
@app.route('/menu')
def menu():
    return 'this is da menu'

#########################################################################
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)