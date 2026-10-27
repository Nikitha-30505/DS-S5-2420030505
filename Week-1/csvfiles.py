#6 : dataframes using files

import pandas as pd
df = pd.read_csv('Iris.csv')
print(df)
print('\n')

#6.1 : dataframes using files
import pandas as pd
df = pd.read_csv('movies.csv')
print(df)
print('\n')

#6.3 : or

import pandas as pd
df = pd.read_csv('titanic.csv', index_col=0) 
print(df)
print('\n')

#7:using json files
import pandas as pd
df = pd.read_json('sample1.json',typ='series')
print(df)
print('\n')
#student data set
import pandas as pd
data = {'s.number': [1, 2, 3, 4, 5],
        's.name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        's.age': [20, 21, 19, 22, 23],
        'section': ['A', 'B', 'A', 'C', 'B'],
        'Branch': ['CSE', 'IT', 'CSE', 'ECE', 'ME']}
df = pd.DataFrame(data)
print(df)
df.to_csv('studentdata.csv')
df.to_json('studentdata.json')
print('\n')

#operations


import pandas as pd
df = pd.read_csv('Iris.csv')
print(df.head())
print()
print(df.head(10))
print()
print(df.tail())
print()
print(df.tail(10))
print()
df.info()
print()
print("Shape:")
print(df.shape)
print()
print("Description:")
print(df.describe())
