import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

import matplotlib
print(matplotlib.get_backend())

def main():
    path = "data/life_expectancy_years.csv"
    db = load(path)
    
    if db is None:
        print(f"Error: Invalid path. {path}")
    else:
        db.dropna(inplace=True)
        france_data = db[db['country'] == "France"].iloc[:, 1:]
        years_data = france_data.columns.astype(int)
        print(france_data.columns)
        # plt.plot(years_data, france_data.values.flatten(), label="France")
        # plt.show()
    


if __name__ == "__main__":
    main()
