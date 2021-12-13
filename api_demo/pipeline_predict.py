import joblib
import config as cfg
import pandas as pd
import numpy as np

#Cargamos modelo y pipeline
churn_model = joblib.load('churn_pipeline.pkl')

#Funcion para hacer predicciones.
def predict(X):

    predicts = churn_model.predict(X)
    print(predicts)
    return predicts[0]