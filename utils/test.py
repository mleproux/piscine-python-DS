import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('data.json')

df.plot()
        
plt.show()