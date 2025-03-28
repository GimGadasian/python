# # while loop
# i = 0
# while True:
#     input_num = int(input("숫자를 입력하세요: "))
#     i += 1
#     if (i > 10):
#         break
    
    
while True:
    print("1. 숫자 맞추기")
    print("2. 로또 맞추기")
    print("3. 성적 프로그램")
    print("0. 종료")
    
    choice = int("원하는 번호를 입력하세요.>> ")

    if (choice == 1):
        print("<숫자 맞추기 프로그램>")
        
    elif (choice == 2):
        print("<로또 맞추기 프로그램>")
        
    elif (choice == 3):
        print("<성적 프로그램>")
    
    elif (choice == 0):
        print("<프로그램 종료>")