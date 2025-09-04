#File (I/O) 읽고 쓰기

#해당 파일 이름으로 파일을 쓰기 모드로 연다
with open('my_file.txt','w',encoding='utf-8') as f:
    f.write("Hello, Mister John Doe!\n")
    f.write("We are really miss you!\n")
    
#해당 파일에 내용 추가 한다    
with open('my_file.txt','a',encoding='utf-8') as f:
    f.write("We are waiting for defence front line\n")
    f.write("Please give me the order")
    
#방금 만든 해당 파이을 읽기모드로 연다
with open('my_file.txt','r',encoding='utf-8') as f:
    content=f.read()
    print("--- File Info ---")
    print(content)
    
    