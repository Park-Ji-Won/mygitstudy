import pandas as pd

#pd.read_csv함수로 해당 csv파일을 읽어 데이터프레임으로 만듬
file_path=r'C:\Users\TFX255GS\Desktop\mygitstudy\Python_real_practice\students.csv'
df=pd.read_csv(file_path)

print(df)

#처음 5개 행 미리보기
print("---------------")
print("---.head()---")
print(df.head())
print("---------------")

#데이터프레임의 전체적인 정보 확인(자료형,누락된 값등)
print("---------------")
print("\n---.info()---")
df.info()
print("---------------")

#숫자형 데이터의 기초 통계량 확인(평균,표준편차,최솟값/최댓값등)
print("---------------")
print("\n---.describe()---")
print(df.describe())
print("---------------")

#특정열(Column)선택
print(df['이름'])
print("---------------")

#두개의 열 선택하기 
#여러열을 선택할때는 대괄호 두번 사용
print(df[['이름','학점']])
print("---------------")

#특정 조건에 맞는 행 선택하기=> 필터링
#조건식 만들기
#해당 열의 값이 2와 같은지 비교->True/False로 결과 도출
conditon=(df['학년']==2)
print("---조건식 결과---")
print(conditon)

#이조건식을 데이터프레임의 대괄호 안에 그대로 삽입
#True인 행만 선택
print("\n---2학년 학생 결과---")
print(df[conditon])

#해당 값 이상의 대상 찾기
print("---------------")
print(df[df['학점']>=3.8])

#여러조건 조합
#&(AND):두 조건이 모두 참일때
#|(OR):두 조건 중 하나라도 참일떄

conditon1=(df['전공']=='컴퓨터')
conditon2=(df['학점']>=3.7)

print("---------------")
print(df[conditon1&conditon2])