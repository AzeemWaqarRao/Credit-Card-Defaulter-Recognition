import os

from DataValidation.data_validation import DataValidation

class TrainValidation:
    def __init__(self,path):
        self.path = path
        self.dv = DataValidation(path, os.path.join("Schema","schema_training.json"))

    def train_validation(self):
        try:

            lengthOfDateStampInFile, lengthOfTimeStampInFile, colName, numberofColumns = \
                self.dv.get_values_from_schema()
            self.dv.validate_filename(lengthOfDateStampInFile,lengthOfTimeStampInFile)
            self.dv.validate_column_length(numberofColumns)


        except Exception as e:
            raise e
