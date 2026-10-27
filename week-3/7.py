import pandas as pd

df = pd.DataFrame({
    'X' : [10,20,30,40,50],
    'Y' : [10,20,30,40,50]
})

corr_mat = df.corr(method='pearson')
print("Pearson Correlation Matrix:\n",corr_mat)