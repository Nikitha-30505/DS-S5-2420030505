# case Normalization
import pandas as pd
df = pd.DataFrame({
    'Name' : ['Alice','BOB','Charlie','DAVID']})
# convert to lower case
df['Name_lower'] = df['Name'].str.lower()


#convert to upper case
df['Name_upper'] = df['Name'].str.upper()
print(df)