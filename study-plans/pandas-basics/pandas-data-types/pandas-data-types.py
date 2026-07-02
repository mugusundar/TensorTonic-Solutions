import pandas as pd

def data_types_overview(data):
    df = pd.DataFrame(data)
    dtypes = df.dtypes.astype(str)
    return{
        "dtypes" : dtypes.to_dict(),
        "type_counts" : dtypes.value_counts().to_dict(),
        "num_columns" : df.shape[1]
    }