# used in common functions i will be using :
import os 
import pandas as pd
import sys
import numpy as np
import dill # help to create the pkl file !!!
from src.exception import CustomException


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