from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/novaPagina/")
def nova_pagina():
    return render_template("segunda-pagina.html")


if __name__ == "__main__":
    app.run(debug=True)