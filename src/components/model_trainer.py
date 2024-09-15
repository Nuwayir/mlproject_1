#model trainer Modular struture:
# will tryin diffrent models ans check the results 
import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

# for every compoonents i need to create config --> path to save the result of it 
@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    
    # to train my model 
class ModelTrainer:
    def __init__(self): # create an object form the previous class to get the reults finally in the path !!
        self.model_trainer_config=ModelTrainerConfig()
        
                # the input is the outout of the DataTransformation:
    def initiate_model_trainer(self,train_array,test_array):#we don't need it yet preprocessor_path
           try:
               logging.info("split training and test input data")
               X_train,y_train,X_test,y_test=(
                   train_array[:,:-1],# take out the last column and keep the other  
                   train_array[:,-1],# y value only 
                   test_array[:,:-1],
                   test_array[:,-1]
               )
               models ={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
               }
               model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                                 models=models)
                ## To get best model score from dict
               best_model_score = max(sorted(model_report.values()))

                ## To get best model name from dict
               best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                ]
               best_model = models[best_model_name]

               if best_model_score<0.6:
                    raise CustomException("No best model found")
               logging.info(f"Best found model on both training and testing dataset")

                
               # do preprocessing_obj= laod the pkl file of transforamition but yet i think we don't need it 
               
               save_object(
                   file_path=self.model_trainer_config.trained_model_file_path,
                   obj=best_model
               )
               
               predicted=best_model.predict(X_test)
               r2_square=r2_score(y_test,predicted)
               return r2_square
               
               
           except Exception as e:
               raise CustomException(e,sys)
            