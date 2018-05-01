from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return "hello World"
    return render_template('index.html')

@app.route('/users/<string:username>')
def users(username):
    return # "hello %s" % username
    render_template('user.html', uname=username)

@app.route('/user')
def user():
    return "this page is for users"

if __name__ == '__main__':
    app.run()
