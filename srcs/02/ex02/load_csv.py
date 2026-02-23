import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except:
        return None