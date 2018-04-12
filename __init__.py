from flask import Flask,request, render_template
from flask import flash
from key import Key
import os

app = Flask(__name__)

@app.route('/')
def index():
    roomKey = generateRootKey()
    return render_template('index.html',key=roomKey)

def generateRootKey():
    key = Key()
    chatPin = key.getKey()
    return chatPin

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/<key>/')
def chat(key):
    flash(u'Bienvenue dans votre chat')
    return render_template('room.html',key=key)

if __name__ == '__main__':
    app.secret_key = 'A7§/23/3KF093250'
    app.run(debug=True)


