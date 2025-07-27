import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.exception import CustomException
from src.logger import logging
import os


@dataclass
class DataTransfromationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransfromation:
    def __init__(self):
        self.data_transfromation_config = DataTransfromationConfig()

    def get_data_transfromation_obj(self):
        '''
        This is where the data transsfmoration is happening
        '''

        try:
            numerical_columns = ['writing_score', 'reading_score']
            categorical_variables = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='median')),
                    ("scaler", StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='mode')),
                    ("one_hot_encoder", OneHotEncoder() ), 
                    ("scaler", StandardScaler())
                    
                ]
            )
            logging.info("Numerical Columns standard scaling completed")
            logging.info("Categorical columns encoding completed")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipelines", cat_pipeline, categorical_variables)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)

