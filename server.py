from flask import Flask, jsonify, request
import time

app = Flask(__name__)

relay_state = "OFF"
wifi_name = "UNKNOWN"
last_seen = time.time()

@app.route("/")
def home():
    return "ESP01S Web Server Running"

@app.route("/relay", methods=["GET"])
def relay():
    global relay_state, wifi_name, last_seen

    # Nhận tên WiFi từ ESP
    if "wifi" in request.args:
        wifi_name = request.args.get("wifi")

    # Điều khiển relay qua URL
    if "state" in request.args:
        if request.args.get("state") == "ON":
            relay_state = "ON"
        elif request.args.get("state") == "OFF":
            relay_state = "OFF"

    last_seen = time.time()

    return jsonify({
        "state": relay_state,
        "wifi": wifi_name,
        "online": True
    })

@app.route("/status")
def status():
    online = (time.time() - last_seen) < 10
    return jsonify({
        "state": relay_state,
        "wifi": wifi_name,
        "online": online
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
