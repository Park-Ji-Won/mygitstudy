#dictionary => key-value pair

phone_book={}
phone_book['홍경래']='010-8819-9021' #공백리스트는 '[]'로 생성 딕셔너리는 '{}' 생성에 유의
print(phone_book)

phone_book={'홍경래':'010-8819-9021'}#딕셔너를 생성과 동시 초기화하는 법
print(phone_book)

phone_book['이인좌']='010-9231-4123'
phone_book['고니시']='013-2434-3245'
print(phone_book)

print(phone_book['이인좌'])#주소록이 같으면 사람이름으로 전화번호 확인가능

phone_book.keys()#딕셔너리에 사용되는 모든키 호출 출력
print(phone_book.keys())

phone_book.values()#딕셔너리에 사용된 모든 값을 호출 출력
print(phone_book.values())

dict={'Name':'홍경래','Age':50,'Major':'군사학 , 용병학'}#리스트와 같이 딕셔너리도 어떤한 유형의
                                                        #값도 저장 가능
                                                        #Ex)정수,문자열,다른 리스트/딕셔너리
                                                        #항목으로 저장가능

print(dict['Name'])
print(dict['Age'])
print(dict['Major'])#한 인물에 관해 딕셔너리로 저장후 호출 출력

#for 반복 루프를 활용하여 모든 항목 방문하면서 출력
for key in sorted(phone_book.keys()): #sorted() 함수를 활용하여 딕셔너리들의 키를 정렬함
    print(key,phone_book[key]) #정렬된 키를 가지고 연관된 값을 출력 정렬된 상태로 출력
    
del phone_book['고니시']#딕셔너리안에 해당 항목을 삭제
print(phone_book)

phone_book.clear()#딕셔너리안의 모든 항목 삭제
print(phone_book)