# debug mode on: export FLASK_ENV=development
# app.py -> application.py: export FLASK_APP=application.py

from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
#create a function to check winning possibilities

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
        #session['winner'] = None

    return render_template('game.html', game=session['board'], turn=session['turn']) #winner=session['winner']

@app.route('/play/<int:row>/<int:col>')
def play(row, col):

    # Play a move
    session['board'][row][col] = session['turn']

    # Check if the move results in a win
    #session['winner'] = function to check game board with winning combinations

    # Determine turn for next move
    if session['turn'] == 'X':
        session['turn'] = 'O'
    else:
        session['turn'] = 'X'

    return redirect(url_for('index'))

