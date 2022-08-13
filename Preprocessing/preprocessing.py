from sklearn.impute import KNNImputer
import pandas as pd

class Preprocessing:

    def __init__(self,path):
        self.path = path

    def preprocess_train(self):

        try:
            df = pd.read_csv("Training_Data.csv")
            X,y = self.split_data(df)

            if self.is_null(X):
                X = self.impute_values(X)
            X = self.drop_zero_std(X)

            X.to_csv("X.csv")
            y.to_csv("y.csv")


        except Exception as e:
            raise e

    def split_data(self,df):

        try:

            df = df.iloc[:, 1:]
            y = df["Target"]
            X = df.drop(["Target"], axis=1)

            return X, y
        except Exception as e:
            raise e

    def is_null(self,df):

        try:
            df = pd.read_csv("Training_Data.csv")
            isNull = False
            null_count = df.isna().sum()
            for i in null_count:
                if i > 0:
                    isNull = True
                    break
            return isNull

        except Exception as e:
            raise e

    def impute_values(self,df):
        try:
            impute = KNNImputer(n_neighbors=5, weights="uniform")
            temp = impute.fit_transform(df)
            data = pd.DataFrame(temp, columns=df.columns)
            return data

        except Exception as e:
            raise e

    def drop_zero_std(self,data):
        try:

            dic = data.describe()

            for i in data.columns:
                if dic[i]['std'] == 0:
                    data = data.drop([i], axis=1)

            return data

        except Exception as e:
            raise e