import glob
import json
import os
import shutil

import pandas
import pandas as pd


class DataValidation:

    def __init__(self,path,schemapath):
        self.path = path
        self.schemapath = schemapath

    def validate_filename(self,lengthOfDateStampInFile, lengthOfTimeStampInFile):

        try:
            for file in os.listdir(self.path):
                filename = str(file)
                if filename.split(".")[1] == "csv":

                    filename = filename.split(".")[0]
                    filename = filename.split('_')

                    if filename[0] == "creditCardFraud" and len(filename[1]) == lengthOfDateStampInFile \
                            and len(filename[2]) == lengthOfTimeStampInFile:
                        shutil.copy(os.path.join(self.path,file),"Good_Raw_File")

                    else:
                        shutil.copy(os.path.join(self.path, file), "Bad_Raw_File")

                else:
                    # wrong extension file
                    pass

        except Exception as e:
            raise e


    def validate_column_length(self, column_length):

        try:
            for file in os.listdir("Good_Raw_File"):
                df = pandas.read_csv(os.path.join("Good_Raw_File",file))

                if df.shape[1] == column_length:
                    # file stays in good files
                    pass
                else:
                    shutil.move(os.path.join("Good_Raw_File",file),"Bad_Raw_File")

        except Exception as e:
            raise e

    def get_values_from_schema(self):
        try:
            f = open(self.schemapath, 'r')
            dic = json.load(f)
            f.close()

            lengthOfDateStampInFile = dic['LengthOfDateStampInFile']
            lengthOfTimeStampInFile = dic['LengthOfTimeStampInFile']
            colName = dic['ColName']
            numberofColumns = dic['NumberofColumns']

            return lengthOfDateStampInFile, lengthOfTimeStampInFile, colName, numberofColumns

        except Exception as e:
            raise e

    def check_missing_columns(self):

        try:
            for file in os.listdir("Good_Raw_File"):
                df = pd.read_csv(os.path.join("Good_Raw_File",file))
                flag = True
                for columns in df:
                    if len(df[columns]) - df[columns].count() == len(df[columns]):
                        flag = False
                        shutil.move(os.path.join("Good_Raw_File",file),os.path.join("Bad_Raw_File"))
                        break
                if flag:
                    df.rename(columns={'default payment next month':'Target'}, inplace=True)
                    df.to_csv(os.path.join("Good_Raw_File",file))

        except Exception as e:
            raise e


    def putNull(self):

        try:
            for file in os.listdir("Good_Raw_File"):
                df = pd.read_csv(os.path.join("Good_Raw_File",file))
                df.fillna("Null",inplace=True)
                df.to_csv(os.path.join("Good_Raw_File",file))

        except Exception as e:
            raise e

    def merge_files(self):
        try:
            files = os.path.join("Good_Raw_File", "*.csv")

            files = glob.glob(files)

            df = pd.concat(map(pd.read_csv, files), ignore_index=True)
            df.iloc[:, 1:].to_csv("Training_Data.csv")
        except Exception as e:
            raise e

    def delete_raw_files(self):

        dir = 'Good_Raw_File'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        dir = 'Bad_Raw_File'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
