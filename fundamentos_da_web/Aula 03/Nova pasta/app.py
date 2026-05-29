from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/perfil/<nome>")
def perfil(nome):
    return render_template("perfil.html", nome = nome, valor=150.00)

if __name__ == "__main__":
    app.run(debug=True)