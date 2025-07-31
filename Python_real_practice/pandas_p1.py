# 리스트를 사용하여 DataFrame 객체 생성하기
import pandas as pd

data = [['A',1],['B',2],['C',3]]
df=pd.DataFrame(data,columns=['col1','col2'])
print(df)

# 딕셔너리를 사용하여 DataFrame 객체 생성하기
data = {'col1':['A','B','C'],'col2':[1,2,3]}
df=pd.DataFrame(data)
print(df)

# CSV 파일을 사용하여 DataFrame 객체 생성하기
#df=pd.read_csv('data.csv')
#print(df)