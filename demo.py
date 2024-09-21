import pandas as pd
import statistics
df=pd.read_csv("demodata.csv")
print(df)
print(df.std(axis=0,skipna=True))

