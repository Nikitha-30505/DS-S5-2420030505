#spearmanr correlation 
import pandas as pd
from scipy.stats import spearmanr

df = pd.DataFrame({
    'sname' : ['A','B','C','D','E'],
    'DS' :[12,24,33,45,60],
    'QC' :[23,34,45,56,67],
    'CD' :[22,33,44,55,66],
    'TOC':[77,88,99,22,33]
})
#print(df.corr(method='pearson',numeric_only=float))
print(df.corr(method='spearman',numeric_only=float))

print()

df = pd.read_csv("Iris.csv")
print(df.corr(method='spearman',numeric_only=float))

print()

df = pd.read_csv("titanic.csv")
print(df.corr(method='spearman',numeric_only=float))

