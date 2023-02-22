from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/contato")
def contatos():
    return render_template("contato.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

if __name__ == "__main__":
    app.run()

