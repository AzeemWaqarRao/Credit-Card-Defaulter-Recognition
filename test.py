import pandas as pd
import json
import os

from DataValidation.data_validation import DataValidation


dir = 'Good_Raw_File'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir = 'Bad_Raw_File'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

#
# dv = DataValidation("Training_Batch_Files","Schema/scheman_training.json")
# dv.validate_filename(8,6)
# dv.validate_column_length(24)
#
#
# #
# df = pd.read_csv("Training_Batch_Files/creditCardFraud_28011965_120215.csv")
#
# print(df.shape[1])
