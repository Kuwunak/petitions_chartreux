from flask import Flask, render_template, send_from_directory, request

app = Flask("petitions")

NOMBRE_DE_SIGNATURES = 0


@app.get("/")
def index():
    return render_template("index.html", nombre_signatures=NOMBRE_DE_SIGNATURES)


@app.post("/")
def sign():
    global NOMBRE_DE_SIGNATURES
    NOMBRE_DE_SIGNATURES += 1
    print(request.form)


@app.get("/style.css")
def sytle():
    return send_from_directory("static", "style.css")
