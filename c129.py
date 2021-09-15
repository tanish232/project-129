import pandas as pd
import csv
df=pd.read_csv('dwarf_stars.csv')
df=df.notna()
df["Radius"] = 0.102763*df["Radius"]
df["Mass"] = 0.000954588*df["Mass"]
print(df.head())
df.to_csv("dwarf_stars_new.csv")