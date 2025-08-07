#데이터 통계
import pandas as pd

data={
    'Student Number':range(2020,2030), #2020번 부터 2030까지 만들기
    'Grade':[100,95,85,90,80,40,50,60,70,70] #각각 인덱스 지정 Grade 라는 인덱스가 만들어짐
}

#주요통계지표
frame=pd.DataFrame(data)
print(frame.describe())
print('-----------------------------')
#데이터구조
print(frame.info())
print('-----------------------------')
#중복 제거
print(frame['Grade'].unique())
print('-----------------------------')
#Group by
print(frame['Grade'].value_counts())
