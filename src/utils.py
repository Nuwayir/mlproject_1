# used in common functions i will be using :
import os 
import pandas as pd
import sys
import numpy as np
import dill # help to create the pkl file !!!
from src.exception import CustomException
from sklearn.metrics import r2_score

from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        # Extracts the directory part from the file_path
        dir_path = os.path.dirname(file_path)# --> artifacts
        
        # Create the directory if it doesn't exist --> with the name of artifacts
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)# to add the obj in hte foldeer --> preprocessor.pkl in artifacts
#pickel
    except Exception as e:
        raise CustomException(e, sys)
def evaluate_models(X_train, y_train,X_test,y_test,models,param):#param
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)
            
            # keep apending the result of evalution of every Model in form of dictionary 
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
    