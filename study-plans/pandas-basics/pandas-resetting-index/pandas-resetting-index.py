import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)
    df2 = df.set_index(index_col)
    df3 = df2.reset_index()
    return [df2.columns.to_list(),df3.columns.to_list()]