"""
Pandas
데이터 조작을 용이하게 하기 위해 다차원 배열에 인덱스를 
지정한 자료구조를 정의하고 정렬, 변환, 삭제 등을 할 수 있는 메서드를 제공

Series - 1차원 데이터 구조 ( 하나의 Row )
DataFrame - 2차원 데이터 구조 ( 여러개의 시리즈가 모여서 생성 )
"""
import pandas as pd

data={
    'Student Number':range(2020,2030), #2020번 부터 2030까지 만들기
    'Grade':[100,95,85,90,80,40,50,60,70,70] #각각 인덱스 지정 Grade 라는 인덱스가 만들어짐
}
print('일반')
print(pd.DataFrame(data))
print('-------------------------')
print(pd.DataFrame(data,columns=['Grade','Student Number']))
print('-------------------------')
print('프레임 인덱스 나열변경')
print(pd.DataFrame(data,columns=['Grade','Student Number'],index=['a','b','c','d','e','f','h','i','j','k']))
print('-------------------------')
print('행렬 변환')
print(pd.DataFrame(data,columns=['Grade','Student Number'],index=['a','b','c','d','e','f','h','i','j','k']).transpose())
print('+++++++++++++++++++++++++')


