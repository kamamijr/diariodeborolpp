from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Estruturas')
def estrutura():
    return render_template('Estruturas.html')

@app.route('/Subprogramas')
def Subprogramas():
    return render_template('Subprogramas.html')

@app.route('/Tratamento')
def Tratamento():
    return render_template('Tratamento.html')

@app.route('/Sintaxe')
def Sintaxe():
    return render_template('Sintaxe.html')

@app.route('/Semântica')
def Semântica():
    return render_template('Semântica.html')


@app.route('/Introdução')
def Introdução():
    return render_template('Introdução.html')
@app.route('/Variáveis')
def Variáveis():
    return render_template('Variáveis.html')
@app.route('/Tipos')
def Tipos():
    return render_template('Tipos.html')
@app.route('/Expressões')
def Expressões():
    return render_template('Expressões.html')

@app.route('/Orientação')
def Orientação():
    return render_template('Orientação.html')
@app.route('/Linguagem')
def Linguagem():
    return render_template('Linguagem.html')
@app.route('/Prolog')
def Prolog():
    return render_template('Prolog.html')

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
