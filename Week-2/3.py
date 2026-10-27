import pandas as pd
import numpy as np

df = pd.DataFrame({'Age' : [25,30,np.nan,40,35],
                   'Department' :['HR','Finance','Finance',np.nan,'IT']})
print("Original Dataset(with missing values):")
print(df)
print('\n')
df_drop_rows = df.dropna()
print("After dropping rows: \n",df_drop_rows)
print('\n')
df_drop_cols = df.dropna(axis=1)
print("\nAfter dropping columns: \n",df_drop_cols)