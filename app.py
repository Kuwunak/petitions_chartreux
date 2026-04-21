from flask import Flask, render_template, send_from_directory, request

app = Flask("petitions")

NB_SIGNATURES = 0

@app.get("/")
def index():
    return render_template("index.html", nombre_signatures=NB_SIGNATURES)


@app.get("/style.css")
def sytle():
    return send_from_directory("static", "style.css")

@app.post("/")
def sign_petition():
    global NB_SIGNATURES
    NB_SIGNATURES += 1
    return render_template("sign.html", name=request.form["name"])
