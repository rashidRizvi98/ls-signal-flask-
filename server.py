from flask import Flask, request, jsonify
import util
import numpy as np
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hi"


@app.route('/api', methods=['POST'])
def predict_status():

    j_data = request.get_json()

    temperature = float(j_data[0][0])
    pressure = float(j_data[0][1])
    humidity = float(j_data[0][2])
    visibility = j_data[0][3]

    print(j_data)
    print(j_data[0][3])

    prediction = np.array2string(util.get_estimated_status(temperature, pressure, humidity, visibility))
    return jsonify(prediction)


if __name__ == "__main__":
    print("Starting flask")
    util.load_saved_artifacts()
    app.run(host="0.0.0.0", port=5000, debug=True)
