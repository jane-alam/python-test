from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return render_template('index.html', the_time=the_time)


if __name__ == '__main__':
    app.run(host='192.168.0.102', debug=True, use_reloader=True)
