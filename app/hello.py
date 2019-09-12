from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template("index.html", user_agent=user_agent)

@app.route('/user/<name>')
def user(name):
    return render_template("users.html", name=name)

@app.route('/demo')
def go_demo_url():
    return redirect("http://rd.thinktron.co:8080")

if __name__ == '__main__':
    app.run(host='192.168.0.156', debug=True)
