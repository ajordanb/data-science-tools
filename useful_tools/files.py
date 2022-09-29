import pandas as pd
from datetime import datetime
import os 

class File():
    def __init__(self, file_name=str, output_name=str, test_dir=str, data_dir=str):
        self.file_name = file_name
        self.output_name = output_name
        self.test_dir = test_dir
        self.data_directory = data_dir

    def json_to_csv(self):
        df = pd.read_json(self.file_name)
        return df.to_csv(
            f"{self.test_dir}/{self.output_name}-{datetime.utcnow().strftime('%Y-%m-%d-%H-%M')}.csv")

    def csv_to_json(self):
        df = pd.read_csv(self.file_name)
        return df.to_json(
            f"{self.test_dir}/{self.output_name}-{datetime.utcnow().strftime('%Y-%m-%d-%H-%M')}.json"
        )

    def json_to_excel(self):
        df = pd.read_json(self.file_name)
        return df.to_excel(
            f"{self.test_dir}/{self.output_name}-{datetime.utcnow().strftime('%Y-%m-%d-%H-%M')}.xslx"
        )

    def excel_to_json(self):
        df = pd.read_excel(self.file_name)
        return df.to_json(
            f"{self.test_dir}/{self.output_name}-{datetime.utcnow().strftime('%Y-%m-%d-%H-%M')}.json"
        )
    def merge_csv_files(self):
        '''Assumes you have created both directories, the data and the one you will use to save these new files
        Aassumes the csv files have the same column definitions. '''
        files = [file for file in os.listdir(f'./{self.data_directory}')]
        df = pd.DataFrame()
        for file in files:
            df_csv = pd.read_csv(f'./{self.data_directory}/'+file)
            input = pd.concat([df,df_csv])
            input.to_csv(f"{self.test_dir}/{self.output_name}-{datetime.utcnow().strftime('%Y-%m-%d-%H-%M')}.csv")
        return input
