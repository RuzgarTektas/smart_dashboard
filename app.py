from flask import Flask, request, render_template_string

app = Flask(__name__)

# Tek bir dictionary ile veri sakla
data = {
    "temperature": None,
    "humidity": None
}

@app.route('/')
def index():
    return render_template_string("""
    <html>
      <head>
        <title>Smart Dashboard</title>
      </head>
      <body>
        <h1>Oda Durumu</h1>
        <p>Sıcaklık: {{ data['temperature'] if data['temperature'] else 'Veri yok' }} °C</p>
        <p>Nem: {{ data['humidity'] if data['humidity'] else 'Veri yok' }} %</p>
      </body>
    </html>
    """, data=data)

@app.route('/update', methods=['GET'])
def update():
    temp = request.args.get('temp')
    hum = request.args.get('humidity')
    if temp is None or hum is None:
        return "Missing params", 400

    # Verileri sakla
    data['temperature'] = temp
    data['humidity'] = hum
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)