

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def bot():
    return render_template("IBM.html");

if  __name__ == '__main__':
    app.run()