from incomeprediction.logger import logging
from incomeprediction.exception import incomepredictionexception
import os, sys 
import pandas as pd 
from incomeprediction.entity.config_entity import *
from incomeprediction.entity.artifact_entity import *
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json



class DataValidation:

    def __init__(self, data_ingestion_artifact:DataIngestionArtifact,
                    data_validation_config:DataValidationConfig):
                    try:
                        logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
                        self.data_ingestion_artifact = data_ingestion_artifact
                        self.data_validation_config = data_validation_config
                    except Exception as e:
                         raise incomepredictionexception (e,sys) from e


    def get_train_and_test_df(self):
        try:
           
            train_df = self.data_ingestion_artifact.train_file_path
            test_df = self.data_ingestion_artifact.test_file_path
            return train_df,test_df
        except Exception as e:
            raise incomepredictionexception (e,sys) from e

    def is_train_test_file_exist(self):
        try:
             logging.info("Checking if training and test file is available")
             is_train_file_exist = False
             is_test_file_exist = False

             train_file_path = self.data_ingestion_artifact.train_file_path
             test_file_path = self.data_ingestion_artifact.test_file_path

             is_train_file_exist = os.path.exists(train_file_path)
             is_test_file_exist = os.path.exists(test_file_path)

             is_available = is_train_file_exist and is_test_file_exist
             logging.info(f"Is train and test file exists?-> {is_available}")

             if not is_available:
                message=f"Training file: {train_file_path} or Testing file: {test_file_path} is not present"
                raise Exception(message)

             return is_available
        except Exception as e:
            raise incomepredictionexception (e,sys) from e

    def get_and_save_data_drift_report(self):
        try:
            pass
        except Exception as e:
            raise incomepredictionexception (e,sys) from e

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            #self.validate_dataset_schema()
            #self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successully."
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise incomepredictionexception (e,sys) from e