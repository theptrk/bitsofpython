# # series - basically numpy arrays
# note a series has an index that can be changed
ser1 = pd.Series(data=[1,2,3,4],index=['USA', 'Germany','USSR', 'Japan'])       
ser1 = pd.Series([1,2,3,4], ['USA', 'Germany','USSR', 'Japan'])       

# operations
ser1.uniques()
ser1.nuniques()
ser1.value_counts()
ser1.uniques()

# apply functions
ser1.apply(lambda x: x*2)
ser1.apply(len)
ser1.sum()

# filtering
df['A'].str.contains("your_substring")

# # dataframes
import pandas as pd
improt numpy as np

df = pd.DataFrame(
    np.random.randn(5,4), 
    index='A B C D E'.split(), 
    columns='W X Y Z'.split())

# access a single column as a Series
df['W'] 

# access a single row as a Series
df.loc['A']

# access sub DataFrame by columns, rows or both
df[['W', 'Z']]
df.loc[['A', 'B']]
df.loc[['A', 'B'],['W', 'Z']]

# type of a column is a panadas Series
type(df['W'])
# pandas.core.series.Series

# create new columns; add columns together
df['new'] = df['W'] + df['Y']

# drop a column; drop a row; do it inplace to mutate
df.drop('new', axis=1, inplace=True)
df.drop('E', axis=0)

# transpose
df.transpose()

# # filtering

# only show DataFrame where W values are > 0
df[df['W']>0]

# and (&) or (|)
df[ (df['W'] > 0) & (df['Y'] > 1) ]
df[ (df['W'] > 0) | (df['Y'] > 1) ]

# # groupby
by_foo = df.groupby('FooColumnName')
by_foo.mean()
by_foo.std()
by_foo.count()
by_foo.describe()

# # concat, merge, join

# # operations

df.sort_values(by='col2') # inplace by default

# drop rows with NaN Values
df.dropna()

# fill rows with NaN Values
df.fillna('FILLED IN')

# pivot tables
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
#
# 	A	B	C	D
# 0	foo	one	x	1
# 1	foo	one	y	3
# 2	foo	two	x	2
# 3	bar	two	y	5
# 4	bar	one	x	4
# 5	bar	one	y	1

df.pivot_table(values='D',index=['A', 'B'],columns=['C'])
# 
#         C	x	y
# A	B		
# bar	one	4.0	1.0
#       two	NaN	5.0
# foo	one	1.0	3.0
#       two	2.0	NaN
