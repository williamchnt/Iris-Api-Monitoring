# load model
import joblib
import numpy as np
import warnings


def load_model():
    return joblib.load('../../models/knn.joblib')

def predict_model(model, data):
    return model.predict(data)[0]

def predict_from_json(model, json_data):
    warnings.filterwarnings('ignore')
    data = np.array(list(json_data.values())).reshape(1, -1)
    return predict_model(model, data)

