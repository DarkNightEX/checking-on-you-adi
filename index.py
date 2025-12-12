from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------- Home Question ----------------
@app.route("/")
def home():
    return render_template("home.html", name="Adie")

# ---------------- Answer Route ----------------
@app.route("/answer", methods=["POST"])
def answer():
    choice = request.form["choice"]
    if choice == "Yes":
        return redirect(url_for("followup"))
    else:
        message = "It's okay Adie. I'm here for you. ❤️"
        return render_template("final.html", message=message)

# ---------------- Follow-up Question ----------------
@app.route("/followup")
def followup():
    return render_template("followup.html")

# ---------------- Final Message ----------------
@app.route("/final", methods=["POST"])
def final():
    choice = request.form["choice"]
    if choice == "Yes":
        message = "Good to knowww! Stay Safe Always ha! 😊"
    else:
        message = "Take care, it's okay to have doubts Adie. ❤️"
    return render_template("final.html", message=message)

# Required for Vercel
def handler(request, *args, **kwargs):
    return app(request.environ, start_response=None)
