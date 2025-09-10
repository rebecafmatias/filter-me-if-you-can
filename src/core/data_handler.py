from pathlib import Path

import pandas as pd


class CSVProcessor:
    def __init__(self, csv_dir: str):
        self.csv_dir = Path(csv_dir)
        self.files = sorted(self.csv_dir.glob("*.csv"))
        self.df = None

    def read_csv(self):
        dfs = []
        for i in self.files:
            temp_df = pd.read_csv(i)
            dfs.append(temp_df)
        self.df = pd.concat(dfs, ignore_index=True)

    def remove_null_values(self):
        self.df = self.df.dropna()

    def filter_by_column(self, column_name, variable_to_filter):
        self.df = self.df[self.df[f"{column_name}"] == variable_to_filter]

    def processing(self, column_name, variable_to_filter):
        self.read_csv()
        self.remove_null_values()
        self.filter_by_column(column_name, variable_to_filter)

        return self.df
