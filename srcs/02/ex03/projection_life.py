import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load

def convert_value(x):
    if pd.isna(x):
        return None
    
    x = x.strip().lower()
    
    if x.endswith('k'):
        return float(x[:-1]) * 1_000
    elif x.endswith('m'):
        return float(x[:-1]) * 1_000_000
    elif x.endswith('b'):
        return float(x[:-1]) * 1_000_000_000
    else:
        return float(x)

def main():
    life_path = "data/life_expectancy_years.csv"
    gross_path = "data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    
    life_data = load(life_path)
    gross_data = load(gross_path)
    
    if life_data is None:
        print(f"Error: Invalid path for life expectancy data. {life_path}")
        exit(1)
    if gross_data is None:
        print(f"Error: Invalid path for gross domestic product data. {gross_path}")
        exit(1)
    try:
        life_data.dropna(inplace=True)
        gross_data.dropna(inplace=True)
        
        print(life_data.columns)
        print(gross_data.columns)
        
        merged = life_data[["country", "1900"]].merge(
            gross_data[["country", "1900"]],
            on="country",
            suffixes=("_life", "_gdp")
        ).dropna()
        
        plt.plot(merged["1900_gdp"], merged["1900_life"], 'o')
    
        
        # plt.legend(loc='lower right')
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        
        ax = plt.gca()
        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, pos: f"{int(x/1000)}k" if x >= 1000 else f"{int(x)}")
        )

        plt.show()
    except Exception:
        print("Error: Invalid or empty data.")
        
        
    

if __name__ == "__main__":
    main()
