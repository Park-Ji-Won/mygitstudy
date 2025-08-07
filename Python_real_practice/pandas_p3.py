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


