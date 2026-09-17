from datetime import date
from flask import Flask, render_template, request
import pyautogui

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/commitar")
def commitar():
    hoje = date.today().strftime("%d/%m/%y")
    msg = None
    
    # Exemplo: ações automatizadas do pyautogui
    # pyautogui.write(f"Commit automático: {hoje}")
    # pyautogui.press("enter")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)