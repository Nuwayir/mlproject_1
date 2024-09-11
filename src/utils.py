# used in common functions i will be using :
import os 
import pandas as pd
import sys
import numpy as np
import dill # help to create the pkl file !!!
from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
#pickel
    except Exception as e:
        raise CustomException(e, sys)