from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/pagina')
def pagina():
    return "Esta es la página en el endpoint /pagina."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
