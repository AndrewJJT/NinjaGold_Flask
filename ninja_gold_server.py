from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "Just a secret key"
@app.route('/')
def index():
    if 'building' not in session:
        session['building'] = None
    if 'totalgold' not in session:
        session['totalgold'] = 0
    if 'adjustgold' not in session:
        session['adjustgold'] = 0
    if 'strg' not in session:
        session['strg'] = ''
    if 'count' not in session:
        session['count'] = 0
    if session['adjustgold'] > 0:
        session['strg'] = "<p style='color:rgb(50, 241, 50)'>You earn " + str(session['adjustgold']) + " gold from " + str(session['building']) + "!</P>" + session['strg']
    if session['adjustgold'] < 0:
        session['strg'] = "<p style='color:rgb(247, 16, 16)'>You lose " + str(session['adjustgold']) + " gold from " + str(session['building']) + ". Ouch!</P>" + session['strg']
    print("route / ninja gold", session['totalgold'], session['adjustgold'])
    return render_template('index.html', message=session['strg'])

@app.route('/process_money', methods =["POST"])
def processaddbut():
    session['count'] += 1
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        session['adjustgold'] = random.randint(10,20)
    elif session['building'] == 'cave':
        session['adjustgold']  = random.randint(5,10)
    elif session['building'] == 'house':
        session['adjustgold']  = random.randint(2,5)
    elif session['building'] == 'casino':
        session['adjustgold']  = random.randint(-50,50)
    session['totalgold'] += session['adjustgold']
    print("process gold, new total ", session['totalgold'], "session[building]", session['building'], "adjusted gold", session['adjustgold'])
    return redirect('/')


@app.route('/destroy_session', methods=["POST"])
def destroy_session():
    session.clear()	
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)
