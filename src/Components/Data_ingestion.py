import os 
import sys

from src.exception import Custom_Exception
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class Data_Ingestion_Config:
    train_data_path= os.path.join("artifacts","train.csv")
    Raw_data_path= os.path.join("artifacts","data.csv")
    test_data_path= os.path.join("artifacts","test.csv")

class Data_Ingestion:
    def __init__(self) -> None:
        self.ingestion_config=Data_Ingestion_Config
    
    def intitiate_data_ingeston(self):
        logging.info("Enter the data ingestion method")
        try:
            df=pd.read_csv("Notebook\Data\StudentsPerformance.csv")
            logging.info("Read the dataset from Local ")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.Raw_data_path,index=False,header=True)

            logging.info("Data splitting intiated")
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion completed")

            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)
        
        
        except Exception as e:
            raise Custom_Exception(e,sys)
        
            raise Custom_Exception(e)

if __name__=='__main__':
    obj=Data_Ingestion()
    obj.intitiate_data_ingeston()
