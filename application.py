# debug mode on: export FLASK_ENV=development
# app.py -> application.py: export FLASK_APP=application.py

from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

from helpers import win, tie

app = Flask(__name__)

# Store session data in temporary directory
app.config['SESSION_FILE_DIR'] = mkdtemp()
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = [[None, None, None], [None, None, None], [None, None, None]]
        session['turn'] = 'X'
        session['winner'] = None
        session['tie'] = False

    return render_template('game.html', game=session['board'], turn=session['turn'], winner=session['winner'], tie=session['tie'])

@app.route('/play/<int:row>/<int:col>')
def play(row, col):
    # Play a move
    session['board'][row][col] = session['turn']

    # Check for winner
    if (win(session['board'])) == True:
        session['winner'] = session['turn']
        session['board'] = [[None, None, None], [None, None, None], [None, None, None]]

    # Check for tie
    if (tie(session['board'])):
        session['tie'] = True
        session['winner'] = None

    # Determine turn for next move
    session['turn'] = 'O' if session['turn'] == 'X' else 'X'
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))
