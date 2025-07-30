import sys #sys.exit()함수를 사용하기위해서다
import random

while True:
    name=input('이름: (종료=>엔터키)')#사용자가 이름을 입력하지 않고 엔터를 입력할시
    if name == "":#name함수에 비어 있게 되기에 
        sys.exit()#소속 if문에서 검사하여 exit()함수를 호출하여 해당 프로그램을 종료하게 된다.
    
    question=input("무엇에 알고싶습니까? ")
    print(name + "님", "\"", question, "\"에 관하여 질문을 주셨군요.")
    print("운명의 주사위를 굴려봅시다....")

    answer=random.randint(1,8)

    if answer ==1:
        print("네 확실합니다. ")

    elif answer ==2:
        print("전망이 좋은 거 같습니다.")

    elif answer ==3:
        print("믿으셔도 됩니다.")

    elif answer ==4:
        print("글쎄입시다? 아닌거 같습니다.")

    elif answer ==5:
        print("한 점의 의심의 여지도 없이 맞습니다.")

    elif answer ==6:
        print("그럼요, 명백히 올바른 선택입니다.")

    elif answer ==7:
        print("제 답변은 False입니다.")

    else:
        print("나중에 다시 물어봅시다.")