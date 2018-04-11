from flask import Flask,request, render_template
from key import Key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def createRoom():
    roomKey = request.form['initial']+generateRootKey()
    return render_template('index.html',key=roomKey)

def generateRootKey():
    key = Key()
    chatPin = key.getKey()
    return chatPin

@app.route('/<key>/')
def chat(key):
    return render_template('room.html', key=key)

if __name__ == '__main__':
    app.run(debug=True)
