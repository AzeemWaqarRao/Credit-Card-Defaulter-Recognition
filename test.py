import glob
import sqlite3

import pandas as pd
import json
import os
from Preprocessing.preprocessing import Preprocessing

from DataValidation.data_validation import DataValidation


dir = 'Good_Raw_File'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir = 'Bad_Raw_File'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

#
# dv = DataValidation("Training_Batch_Files","Schema/schema_training.json")
# dv.validate_filename(8,6)
# dv.validate_column_length(24)
# dv.check_missing_columns()
# dv.putNull()
# dv.merge_files()


# #
# df = pd.read_csv("Training_Batch_Files/creditCardFraud_28011965_120215.csv")
#
# for columns in df:
#     print(len(df[columns]))
#     print(df[columns].count())

pr = Preprocessing("Training_Data.csv")
pr.preprocess_train()
