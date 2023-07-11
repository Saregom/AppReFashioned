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

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return redirect(url_for('home'))
    
    return render_template('signin.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = [{'Nombre':'Pantalon', 'Precio':50000}, 
                {'Nombre':'Camisa', 'Precio':20000}]

    return render_template('products.html', products = products)

if __name__ == '__main__':
    app.run()