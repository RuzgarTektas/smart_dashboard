from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# Veri saklamak için dictionary
data = {
    "temperature": None,
    "humidity": None
}

# Ana sayfa: HTML + JS ile canlı güncelleme
@app.route('/')
def index():
    return render_template_string("""
    <html>
      <head>
        <title>Smart Dashboard</title>
        <script>
          async function fetchData() {
            try {
              const response = await fetch('/data');
              const json = await response.json();
              document.getElementById('temp').innerText = json.temperature;
              document.getElementById('hum').innerText = json.humidity;
            } catch(err) {
              console.error("Veri alınamadı:", err);
            }
          }

          setInterval(fetchData, 5000); // her 5 saniye veri çek
          window.onload = fetchData;     // sayfa açılır açılmaz veri çek
        </script>
      </head>
      <body>
        <h1>Oda Durumu</h1>
        <p>Sıcaklık: <span id="temp">Veri yok</span> °C</p>
        <p>Nem: <span id="hum">Veri yok</span> %</p>
      </body>
    </html>
    """)

# ESP32 veriyi bu route'a GET ile gönderecek
@app.route('/update', methods=['GET'])
def update():
    temp = request.args.get('temp')
    hum = request.args.get('humidity')
    if temp is None or hum is None:
        return "Missing params", 400

    data['temperature'] = temp
    data['humidity'] = hum
    return "OK", 200

# JSON endpoint: JS buradan veri çekiyor
@app.route('/data', methods=['GET'])
def data_endpoint():
    return jsonify({
        "temperature": data.get("temperature", "Veri yok"),
        "humidity": data.get("humidity", "Veri yok")
    })

if __name__ == '__main__':
    app.run(debug=True)