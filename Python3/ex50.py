from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = 'Hello World'
    return render_template('ex50_index.html',greeting=greeting)

if __name__ =='__main__':
    app.run()
