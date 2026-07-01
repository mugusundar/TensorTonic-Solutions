import pandas as pd

def inspect_dataframe(data):
    df = pd.DataFrame(data)
    return {
        "rows": df.shape[0],
        "cols": df.shape[1],
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "total_values": df.size
    }