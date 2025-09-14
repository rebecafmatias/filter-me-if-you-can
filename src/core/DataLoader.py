import os

import pandas as pd


class CSVProcessor:
    def __init__(self, csv_path: str):
        self.previous_files = []
        self.folder_path = csv_path

    def create_path(self):

        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_new_files(self):
        files = os.listdir(self.folder_path)
        for file in files:
            if file not in self.previous_files:
                new_files = file

        if new_files:
            print(f"New files detected: {new_files}")
            self.previous_files = files
        else:
            print("No new files detected.")

    def read_csv(self):
        dfs = []
        for file_path in self.previous_files:
            path = f"{self.folder_path}/{file_path}"
            data = pd.read_csv(path)
            dfs.append(data)

        if dfs:
            self.combinated_df = pd.concat(dfs, ignore_index=True)
            return self.combinated_df
        else:
            return None

    def processing(self):
        self.create_path()
        self.check_new_files()
        return self.read_csv()
