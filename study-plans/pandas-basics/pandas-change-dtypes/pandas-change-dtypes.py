import pandas as pd

def change_dtype(data, column, target_type):
    df = pd.DataFrame(data)
    dtypes_before = df.dtypes.astype(str).to_dict()

    df_after = df.copy()
    df_after[column] = df_after[column].astype(target_type)
    dtypes_after = df_after.dtypes.astype(str).to_dict()

    return [dtypes_before, dtypes_after]