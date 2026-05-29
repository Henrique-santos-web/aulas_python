from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Bem-vindo ao meu site!"

@app.route("/sobre")
def pagina_sobre():
    return "Criando na aula 47"

if __name__ == "__main__":
    app.run(debug=True)