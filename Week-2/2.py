#forward fill
import pandas as pd
import numpy as np

df = pd.DataFrame({'Age' : [25,30,np.nan,40,35],
                   'Department' :['HR','Finance','Finance',np.nan,'IT']})
print("Original Dataset(with missing values):")
print(df)
df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print('\nForward Fill Dataset:')
print(df_ffill)

df_bfill = df.copy()
df_bfill.bfill(inplace=True)
print('\nBackward Fill Dataset:')
print(df_bfill)