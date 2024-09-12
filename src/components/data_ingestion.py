
# start the modular structure :
# data sources 
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# after I Done the Datatransformation file:
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# input for the data ingestion part we need this :

@dataclass # decorator 
class DataIngestionConfig:# to defien variables we use init but Here directally 
    train_data_path: str=os.path.join('artifacts',"train.csv")# train: output will savd in this path 
    test_data_path: str=os.path.join('artifacts',"test.csv")#....
    raw_data_path: str=os.path.join('artifacts',"data.csv")#....

class DataIngestion:
    # Initializes the class and stores the configuration object in self.ingestion_config.
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()   # the variable of the above class 
                                                        # i will have access to the three variables above by using this ingestion_congif
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')# mangoDB or whaterver ..
            logging.info("Read the dataset as Datafram")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Train test split initiated")
            
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('Data Ingestion Completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )# for the next step 
        except Exception as e:
            raise CustomException(e,sys)
            
            
if __name__=="__main__":
    obj=DataIngestion()
    # after i've done the dataTransformation i addd these 
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()  
    data_transformation.initiate_data_tarnsformation(train_data,test_data)  
 
 # now run it : python src/components/data_ingestion.py
 