from flask import Flask, render_template, request
from lexer import analizar_lexico
from parser import analizar_sintactico

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tokens = []
    estructuras = []

    if request.method == 'POST':
        codigo = request.form['codigo']
        
        tokens = analizar_lexico(codigo)
        
        estructuras = analizar_sintactico(tokens)

    return render_template('index.html', tokens=tokens, estructuras=estructuras)

if __name__ == '__main__':
    app.run(debug=True)