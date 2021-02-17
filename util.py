import json
import pickle
import numpy as np

__visibility = None
__model = None


def get_estimated_status(temperature, pressure, humidity, visibility):

    try:
        visibility_index = __data_columns.index(visibility.lower())

    except:
        visibility_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = temperature
    x[1] = pressure
    x[2] = humidity
    if visibility_index >= 0:
        x[visibility_index] = 1

    return __model.predict_proba([x])[:, 1]


def get_visibility_names():
    return __visibility


def load_saved_artifacts():
    print("loading artifacts...")
    global __data_columns
    global __visibility

    with open("./artifacts/columns2.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __visibility = __data_columns[3:]

    global __model
    with open("./artifacts/signalfailure_model2.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("artifacts are loaded")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_visibility_names())
    print(get_estimated_status(25, 1012.87, 94, 'light rain'))
