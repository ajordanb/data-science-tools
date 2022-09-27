import pandas as pd
from datetime import datetime


class File():
    def __init__(self, file_name=str, output_name=str, test_dir=str):
        self.file_name = file_name
        self.output_name = output_name
        self.test_dir = test_dir

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
