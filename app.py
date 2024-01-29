from flask import Flask, render_template
import os

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
    # Use environment variable for the secret key
    app.secret_key = os.environ.get("NOVEMBER", "NOVEMBER")

    # Use environment variable for production mode
    app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", False)

    # Change to ssl_context=None during development; use a valid SSL certificate in production
    app.run(host='0.0.0.0', port=5000, ssl_context=None)