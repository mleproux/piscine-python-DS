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
    path = "data/population_total.csv"
    db = load(path)
    
    if db is None:
        print(f"Error: Invalid path. {path}")
        exit(1)
    try:
        main_country = "France"
        other_country = input("Please provide a country : ")
        
        main_country = main_country.lower().capitalize()
        other_country = other_country.lower().capitalize()
        
        db.dropna(inplace=True)
        france_data = db[db['country'].str.lower() == main_country.lower()].iloc[:, 1:]
        other_data = db[db['country'].str.lower() == other_country.lower()].iloc[:, 1:]
        years_data = france_data.columns.astype(int)
        
        france_data = france_data.map(convert_value)
        other_data = other_data.map(convert_value)
        
        plt.plot(years_data, other_data.values.flatten(), label=other_country, color = 'b')
        plt.plot(years_data, france_data.values.flatten(), label=main_country, color = 'g')
        plt.legend(loc='lower right')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        
        ax = plt.gca()
        ax.yaxis.set_major_locator(ticker.MultipleLocator(20_000_000))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/1_000_000:.0f}M'))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
        ax.set_xlim(1800, 2040)

        plt.show()
    except Exception:
        print("Error: Invalid or empty data.")
        
        
    

if __name__ == "__main__":
    main()
