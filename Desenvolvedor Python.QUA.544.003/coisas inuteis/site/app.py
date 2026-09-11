from flask import Flask, render_template

app = Flask(__name__)


# Rota da Página Principal (com a animação e os botões)
@app.route("/")
def index():
  return render_template("index.html")


# Rotas para as 4 páginas/jogos adicionais
@app.route("/pagina1")
def pagina1():
  return render_template("pagina1.html")


@app.route("/pagina2")
def pagina2():
  return render_template("pagina2.html")


@app.route("/pagina3")
def pagina3():
  return render_template("pagina3.html")


@app.route("/pacman")
def pacman():
  return render_template("pacman.html")


if __name__ == "__main__":
  app.run(debug=True)