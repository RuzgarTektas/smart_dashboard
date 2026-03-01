from flask import Flask, render_template

app = Flask(__name__)

# Örnek değerler (sabit)
current_temp = 24.5
current_humidity = 55.2

@app.route("/")
def home():
    return render_template("index.html", temp=current_temp, humidity=current_humidity)

if __name__ == "__main__":
    app.run()