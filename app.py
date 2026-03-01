from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Smart Home Panel</h1>
    <p>Projem çalışıyor 🔥</p>
    """

if __name__ == "__main__":
    app.run()