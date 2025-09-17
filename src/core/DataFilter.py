def filter_by_column(df, column_name, variable_to_filter):
    return df[df[f"{column_name}"] == variable_to_filter]
