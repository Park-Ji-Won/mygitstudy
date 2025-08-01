import pandas as pd

data = {'col1':['A','B','C'],'col2':[1,2,3]}
df=pd.DataFrame(data)
print(df)

df['col1']
df[['col1','col2']]

df.loc[0]
df.loc[[0,1,2]]

df['col3'] = [4,5,6]

df.loc[3]=['D',4,5]

df.drop(3,inplace=True)

df.rename(columns={'col1':'new_col1'},inplace=True)