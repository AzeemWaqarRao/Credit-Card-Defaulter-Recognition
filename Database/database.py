import os

import pandas as pd
import sqlite3


class Database:

    def __init__(self,dbname):
        self.path = "Training_Data.csv"
        self.df = pd.read_csv(self.path)
        self.dbname = dbname

    def create_connection(self):
        try:
            conn = sqlite3.connect(os.path.join("Database", self.dbname))
            return conn

        except Exception as e:
            raise e

    def create_table(self):
        try:
            conn = self.create_connection()
            self.df.to_sql("data_table", conn, if_exists="replace")
            conn.execute()
            conn.close()

        except Exception as e:
            raise e