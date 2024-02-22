import os
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

import rampwf as rw

problem_title = "Ocean Wave Forecast"

Predictions = rw.make_regression()
workflow = rw.workflows.Regressor()

score_types = [
    rw.score_types.NormalizedRMSE(name="rmse", precision=2),
]

_target_column_name = "VPED"
_ignore_column_names = ["time"]


def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, "data", f_name))
    y_array = data[_target_column_name].values
    X_df = data.drop([_target_column_name] + _ignore_column_names, axis=1)
    return X_df, y_array


def get_train_data(path="."):
    f_name = "train.csv"
    return _read_data(path, f_name)


def get_test_data(path="."):
    f_name = "test.csv"
    return _read_data(path, f_name)


def get_cv(X, y):
    cv = StratifiedShuffleSplit(n_splits=8, test_size=0.2, random_state=42)
    return cv.split(X, y)
