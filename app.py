from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! Este é um teste do servidor LGPD no tablet."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
