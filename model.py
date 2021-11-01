import joblib
import matplotlib as plt
import pandas as pd
import numpy as np
import os
from xgboost import XGBRegressor
from sklearn.model_selection import RandomizedSearchCV

#capture the path of current folder
curr_path = os.path.dirname(os.path.realpath(__file__))



feat_cols = ['Distance','Haversine','Phour','Pmin','Dhour','Dmin','Temp','Humid','Solar','Dust']

xgb_final = joblib.load(curr_path + "/final_model_best.joblib")

#xgb_final = joblib.load('final_model_best.joblib')
#print(xgb_final)

# predicting function
def predict_duration(attributes : np.ndarray):
    """Return Bike Prediction Value"""

    pred = xgb_final.predict(attributes)
    print("Duration Predicted : ")
    return (int(pred[0]))
