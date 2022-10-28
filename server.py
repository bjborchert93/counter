from crypt import methods
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def visit_counter():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    visits = session['visits']

    return render_template('index.html',visits=visits)

@app.route('/redir')
def redir():
    print(session['visits'])
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":    
    app.run(debug=True)