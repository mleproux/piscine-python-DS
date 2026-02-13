import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def main():
    path = "data/life_expectancy_years.csv"
    db = load(path)
    
    if db is None:
        print(f"Error: Invalid path. {path}")
    else:
        test = db["country"]
        db.plot()
        
        plt.show()
    


if __name__ == "__main__":
    main()
