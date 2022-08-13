from Preprocessing.preprocessing import Preprocessing
from TrainValidation.train_validation import TrainValidation


tv = TrainValidation("Training_Batch_Files")
tv.train_validation()


pr = Preprocessing("Training_Data.csv")
pr.preprocess_train()


