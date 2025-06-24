from flask import Flask, render_template, request
from calc_logic import evaluate_expression
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expression = request.form.get("expression")
        result = evaluate_expression(expression)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from environment
    app.run(host="0.0.0.0", port=port)        # Bind to 0.0.0.0 for Heroku
