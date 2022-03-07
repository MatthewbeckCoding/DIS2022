from flask import Flask, render_template, request, redirect, url_for, session, flash
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myverysecretkey'

def check_for_winner(a, b):
    d = (5 + a - b) % 5
    if d == 1 or d == 3:
        result = "player"
    elif d == 2 or d == 4:
        result = "computer"
    elif d == 0:
        result = "tie"
    return result

@app.route("/")
def index():
    if request.args.get('a'):
        a = int(request.args.get('a'))
        b = int(random.randint(0, 4))
        r = (check_for_winner(a, b))

        if r == "player":
            session['player_score'] += 1
            flash('you won')
        elif r == "tie":
            flash('it was a tie')
        else:
            session['computer_score'] += 1
            flash('you lost')

        if session['player_score'] == 3:
            flash('you won the first to three')
            session['gameon'] = False
        elif session['computer_score'] == 3:
            flash('you lost the first to three')
            session['gameon'] = False

        options2 = ["rock", "paper", "scissors", "spock", "lizard"]
        for i in range(len(options2)):
            if a == i and b == i:
                b_selection = options2[i]
                session['choose_computer'] = b_selection
                a_selection = options2[i]
                session['choose_player'] = a_selection
            elif b == i:
                b_selection = options2[i]
                session['choose_computer'] = b_selection
            elif a == i:
                a_selection = options2[i]
                session['choose_player'] = a_selection

    else:
        session['gameon'] = True
        session['player_score'] = 0
        session['computer_score'] = 0
        session['choose_player'] = ""
        session['choose_computer'] = ""
        flash('New game started!')

    return render_template('task3.html', gameon=session['gameon'], computer_score=session['computer_score'],
                           player_score=session['player_score'], choose_player=session['choose_player'],
                           choose_computer=session['choose_computer'])

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    app.run(host, port, debug=True)
