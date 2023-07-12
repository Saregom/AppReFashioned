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

@app.route('/orders')
def orders():
    orders = [{'IdPedido':234, 'Total':50000, 'Fecha':'2023/07/11',
               'Productos':[
                    {'Nombre':'Pantalon', 'Precio':50000}, 
                    {'Nombre':'Camisa', 'Precio':20000}]
            }]
    
    return render_template('orders.html', orders = orders)

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/update-account', methods=['GET', 'POST'])
def updateAccount():
    if request.method == 'POST':
        return redirect(url_for('account'))
    
    return render_template('updateAccount.html')

if __name__ == '__main__':
    app.run()