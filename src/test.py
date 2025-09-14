import os
from pathlib import Path

from core.DataLoader import CSVProcessor

# import schedule
# import time


def main():

    database = "data"
    target_schema = "processed"
    origin_schema = "raw"
    file_name = "output.csv"

    raw_data_dir = Path(__file__).resolve().parents[1] / database / origin_schema
    processed_data_dir = Path(__file__).resolve().parents[1] / database / target_schema

    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)

    processor = CSVProcessor(raw_data_dir)
    final_df = processor.processing()

    output_file_path = os.path.join(processed_data_dir, file_name)
    final_df.to_csv(output_file_path, index=False)


# def main():
#     processing_data()
#     schedule.every(10).seconds.do(processing_data)

#     try:
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Stopped by user.")


if __name__ == "__main__":

    main()
