from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/home')
def home():
    return render_template('home.html', navbar = True)

if __name__ == '__main__':
    app.run()