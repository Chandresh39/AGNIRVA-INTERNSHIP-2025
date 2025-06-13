from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "90cb6920664ee6ee82020c124903c563"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City name is required"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = response.json()
    return jsonify({
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    app.run(debug=True)