from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Debugowo: Flask domyślnie działa na http://127.0.0.1:5000
    # getUserMedia działa na localhost przez HTTP bez HTTPS — do testów lokalnych OK.
    app.run(host="0.0.0.0", port=5000, debug=True)
