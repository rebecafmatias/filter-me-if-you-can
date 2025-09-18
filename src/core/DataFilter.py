def filter_by_column(df, column_name, variable_to_filter):
    try:
        df = df[df[f"{column_name}"] == variable_to_filter]
    except TypeError:
        df = df
    return df
