import sys
from dataclasses import dataclass
import os
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer# if i have misssing value one of the teqhniques
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler 

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

# to provide the input i may required in DataTransformation file : 
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl") 
    #the data will be in preprocessor_obj_file_path saved as preprocessor.pkl in this folder artifacts

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
           
#to cearte all pkl that will be responebile to do the converting:
    def get_data_transformer_object(self):
        '''
         This function responsible for data transformation
        '''

        try:
            numerical_columns=["writing_score","reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"      
            ]
            num_pipline=Pipeline(# run on train when fit_transform()
                steps=[# Handling the missing values & doing the sclaer
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                    ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))# Set with_mean=False here beacuse it categorical 
                    ]
                )
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            # combine all together:
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor

            
        except Exception as e:
            raise CustomException(e,sys)
        #to do the tranformation:
        
    def initiate_data_tarnsformation(self,train_path,test_path):# from data_ingestion
        '''
        This method is responsible for performing data transformation on the training and test datasets. It takes two inputs:

            train_path: The file path to the training data.
            test_path: The file path to the testing data.
        '''
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")
            
            logging.info("Obtaining preprocessing object")
            
            preprocessing_obj=self.get_data_transformer_object()
            
            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]
            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]# target vaiable as it is no Changed 

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]# target vaiable as it is no Changed 
            
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            #combine the features :  merging the input features and their corresponding target valuest
            train_arr = np.c_[ # np.c_ used to merge two arrrays 
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                # i can say only file_path --> from above it same :)
                self.data_transformation_config.preprocessor_obj_file_path,# means -->preprocessor.pkl 
            )
        except Exception as e:
            raise CustomException(e,sys)