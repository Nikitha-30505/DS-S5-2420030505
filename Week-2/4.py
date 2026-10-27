import pandas as pd
df = pd.DataFrame({'ID' : [1,2,2,3,4,4],
                   'Name' : ['Alice','Bob','Bob','Charlie','David','David'],
                   'Age' : [25,30,30,35,40,40]
})
print()
print("Original Dataset:\n",df )
df_exact = df.drop_duplicates()
print("\nAfter removing duplicates:\n",df_exact)

#specifying subset 
print()

df_subset_id = df.drop_duplicates(subset=['ID'])
print("\nAfter removing duplicates based on (ID):\n",df_subset_id)
print()
df_subset_name = df.drop_duplicates(subset=['Name'])
print("\nAfter removing duplicates based on (Name):\n",df_subset_name)