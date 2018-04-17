from flask import Flask,request, render_template, session, url_for,redirect,flash
from key import Key
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    generate = request.form.get('generate', 'False')
    
    if(generate == 'Generer un chat'):
        if('roomKey' in session):
            return redirect(url_for('room',key=session['roomKey']))
        else:
            initial = request.form.get('initial')
            session['roomKey'] = initial.upper() +  generateRouteKey()
            return redirect(url_for('room',key=session['roomKey']))
    else:
        return render_template('index.html')

def generateRouteKey():
    key = Key()
    RouteKey = key.getKey()
    return RouteKey


@app.route('/contact/',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return "Vous avez envoyé : {msg}".format(msg=request.form.get('msg', 'valeur par défaut'))
    return render_template('contact.html')


@app.route('/<key>/')
def room(key):
    return render_template('room.html',key=key)


@app.route('/test/')
def test():
    return 'a'


if __name__ == '__main__':
    SESSION_PERMANENT=False
    app.secret_key = 'A7§/23/3KF093250'
    app.run(debug=True)