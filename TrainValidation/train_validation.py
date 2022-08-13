import os
from Database.database import Database
from DataValidation.data_validation import DataValidation

class TrainValidation:
    def __init__(self,path):
        self.path = path
        self.dv = DataValidation(path, os.path.join("Schema","schema_training.json"))
        self.db = Database("Training_Data.db")

    def train_validation(self):
        try:

            lengthOfDateStampInFile, lengthOfTimeStampInFile, colName, numberofColumns = \
                self.dv.get_values_from_schema()
            self.dv.validate_filename(lengthOfDateStampInFile,lengthOfTimeStampInFile)
            self.dv.validate_column_length(numberofColumns)
            self.dv.check_missing_columns()
            self.dv.putNull()
            self.dv.merge_files()
            self.dv.delete_raw_files()
            self.db.create_table()


        except Exception as e:
            raise e
