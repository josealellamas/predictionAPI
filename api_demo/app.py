from flask import Flask, jsonify, request
import pandas as pd

import config as cfg
import pipeline_predict as pp

app = Flask(__name__)

#ruta para predecir.
@app.route("/predecir", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    data = data[cfg.FEATURES]
    data['area_code'] = data['area_code'].astype('O')
    resultado = pp.predict(data)
    print(resultado)
    return jsonify({"Prediccion": int(resultado)})