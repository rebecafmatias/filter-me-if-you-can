import os
import time
from pathlib import Path

import schedule

from src.core.DataFilter import filter_by_column
from src.core.DataLoader import CSVProcessor


def processing_data():

    database = "data"
    output_file_name = "output.csv"
    column_to_filter = "city"
    variable_filtered = "Curitiba"

    origin_schema = Path(__file__).resolve().parents[1] / database / "raw"
    target_schema = Path(__file__).resolve().parents[1] / database / "processed"

    if not os.path.exists(target_schema):
        os.makedirs(target_schema)

    processor = CSVProcessor(origin_schema)
    final_df = processor.processing()

    try:
        final_df = filter_by_column(final_df, column_to_filter, variable_filtered)
    except NameError:
        print("No columns to filter were found.")
    except KeyError:
        print("No columns to filter were found.")

    try:
        final_df.to_csv(target_schema / output_file_name, index=False)
    except AttributeError:
        print(
            f"""Your object is a {type(final_df)}. You must enter a dataframe in
            order to complete a filtering operation."""
        )


def main():
    processing_data()
    schedule.every(2).seconds.do(processing_data)

    try:
        while True:
            schedule.run_pending()
            time.sleep(2)
    except KeyboardInterrupt:
        print("Stopped by user.")


if __name__ == "__main__":

    main()
