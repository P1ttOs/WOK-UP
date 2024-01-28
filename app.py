from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("acasa.html")

@app.route("/meniu")
def meniu():
    return render_template("meniu.html")

@app.route("/despreNoi")
def despreNoi():
    return render_template("despreNoi.html")

@app.route("/prezentareaFirmei")
def prezentareaFirmei():
    return render_template("prezentareaFirmei.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')  # Change to ssl_context=None or remove ssl_context
