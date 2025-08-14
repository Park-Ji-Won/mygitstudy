import numpy as np

#Python 리스트
my_list=[1,2,3,4,5]

#Numpy 배열로 변환
my_array=np.array(my_list)

print(f"파이썬 리스트: {my_list}")
print(f"Numpy 배열: {my_array}")

#벡터화연산(Vectorized Operation)
doubled_list=[]
for item in my_list:
    doubled_list.append(item*2)
print(f"리스트 연산 결과: {doubled_list}")

#Numpy 배열의 각요소에 2를 곱하려면?
#그냥 배열에 곱하기만 하면 끝
doubled_array=my_array*2
print(f"numpy 배열 연산 결과: {doubled_array}")

