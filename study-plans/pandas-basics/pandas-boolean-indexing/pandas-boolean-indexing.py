import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    pass
    df = pd.DataFrame(data)
    mask = df[column] > threshold
    df2 = df[mask]
    
    return {
        "filtered_data": df2.to_dict(orient="list"),
        "count":df2.shape[0]
    }