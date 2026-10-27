#1
import pandas as pd
data = {
    'apple': [3, 2, 0, 1],
    'orange': [0, 3, 7, 2]
}
df = pd.DataFrame(data)
print(df)
print('\n')
#2

import pandas as pd
data = {
    'apple': [3, 2, 0, 1],
    'orange': [0, 3, 7, 2]
}
df = pd.DataFrame(data,index = ['A', 'B', 'C', 'D'])
print(df)
print('\n')
#3

import pandas as pd
data = {
    'apple': [3, 2, 0, 1],
    'orange': [0, 3, 7, 2]
}
df = pd.DataFrame(data,index = ['A', 'B', 'C', 'D'])
print(df.loc['B'])
print('\n')

#4: dataframes using columns 
import pandas as pd
data = {'col1': [3,2,1,0], 'col2': ['a','b','c','d']}
df = pd.DataFrame.from_dict(data)
print(df)
print('\n')

#5: dataframes using  rows
import pandas as pd
data = {'row1': [3,2,1,0], 'row2': ['a','b','c','d']}
df = pd.DataFrame.from_dict(data, orient='index')
print(df)   
print('\n')

#adding columns
import pandas as pd
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)

print("Adding a new column by passing as Series:")
df['three'] = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(df)
print('\n')

print("Adding a new column using the existing columns in DataFrame:")
df['four'] = df['one'] + df['three']    
print(df)

#for deletion of columns
import pandas as pd

d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
    'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])
}

df = pd.DataFrame(d)
print('Our DataFrame is:')
print(df)
#using del function
print("Deleting the first column using DEL function:")
del df['one']
print(df)
#using pop function
print("Deleting another column using POP function:")
df.pop('two')
print(df)