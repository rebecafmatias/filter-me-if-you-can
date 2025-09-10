from pathlib import Path

from core.data_handler import CSVProcessor


def main():
    raw_data_dir = Path(__file__).resolve().parents[1] / "data" / "raw"
    processed_data_dir = Path(__file__).resolve().parents[1] / "data" / "processed"

    column_name = "city"
    variable = "Curitiba"

    processor = CSVProcessor(raw_data_dir)
    df_filtered = processor.processing(column_name, variable)

    print("Data Filtered:")
    print(df_filtered)

    # Salva resultado
    output_file = processed_data_dir / "saida_filtrada.csv"
    df_filtered.to_csv(output_file, index=False)
    print(f"Result saved at: {output_file}")


if __name__ == "__main__":
    main()
