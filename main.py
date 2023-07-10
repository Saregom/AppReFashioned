from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bienvenido a la app de ReFashioned.'

if __name__ == '__main__':
    app.run() 