from flask import Flask,request, render_template
from key import Key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact/')

def contact():
    return "hello"

key = Key()
chatPin = key.getKey()
root = '/'+chatPin+'/'
print(chatPin)
@app.route(root)
def echo():
    return render_template('index.html', pin=chatPin)

if __name__ == '__main__':
    app.run(debug=True)
