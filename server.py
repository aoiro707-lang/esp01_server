@app.route("/relay", methods=["GET", "POST"])
def relay():
    global relay_state, wifi_name, esp_online

    if request.method == "POST":
        data = request.get_json()
        if data:
            if data.get("state") in ["ON", "OFF"]:
                relay_state = data["state"]
            if "wifi" in data:
                wifi_name = data["wifi"]
            esp_online = True

        return jsonify({
            "state": relay_state,
            "wifi": wifi_name,
            "online": esp_online
        })

    return jsonify({
        "state": relay_state,
        "wifi": wifi_name,
        "online": esp_online
    })
