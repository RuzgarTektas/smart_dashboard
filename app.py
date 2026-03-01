from flask import Flask, request, render_template_string

app = Flask(__name__)

# Global değişkenler (en son veriyi saklamak için)
temperature = None
humidity = None

@app.route('/')
def index():
    return render_template_string("""
    <html>
      <head>
        <title>Smart Dashboard</title>
      </head>
      <body>
        <h1>Oda Durumu</h1>
        <p>Sıcaklık: {{ temp if temp is not None else 'Veri yok' }} °C</p>
        <p>Nem: {{ hum if hum is not None else 'Veri yok' }} %</p>
      </body>
    </html>
    """, temp=temperature, hum=humidity)

# ESP32 bu route'u kullanarak veri gönderecek
@app.route('/update', methods=['GET'])
def update():
    global temperature, humidity
    temp = request.args.get('temp')
    hum = request.args.get('humidity')
    if temp and hum:
        temperature = temp
        humidity = hum
        return "OK", 200
    return "Missing params", 400

if __name__ == '__main__':
    app.run(debug=True)