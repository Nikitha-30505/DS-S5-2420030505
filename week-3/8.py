#for data sets
import pandas as pd
df = pd.read_csv("Iris.csv")
print(df.corr(method='pearson',numeric_only=float))

print()

df = pd.read_csv("titanic.csv")
print(df.corr(method='pearson',numeric_only=float))