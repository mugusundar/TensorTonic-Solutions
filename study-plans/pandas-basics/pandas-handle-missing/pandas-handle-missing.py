import pandas as pd

def handle_missing(data, fill_value):
    df = pd.DataFrame(data)
    null_counts_dict = df.isnull().sum().to_dict()
    cleaned_data_dict = df.fillna(fill_value).to_dict(orient="list")

    return {
        "null_counts": null_counts_dict,
        "cleaned_data": cleaned_data_dict
    }