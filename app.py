from flask import Flask, render_template

app = Flask(__name__)

# Örnek sıcaklık değeri
current_temp = 24.5

@app.route("/")
def home():
    return render_template("index.html", temp=current_temp)

if __name__ == "__main__":
    app.run()