# 1부터 100까지 랜덤숫자 생성, 정답 맞추는 프로그램
#********************************************
#도전횟수: 5
#도전번호: 1, 2, 3, 4, 5
#랜덤번호: 5

#1 랜덤숫자 생성
#2 입력값 리스트 생성
#3 num 변수(반복횟수) 선언
#4 10번 질문 반복
#5 입력값 리스트에 넣기
#6 조건들 생성
#7 맞추면 프로그램 종료
#8 못 맞추면 반복문 밖에서 출력값들 정리

import random
ran_num = random.randint(1, 101)
input_nums = []
num = 0
for num in range(1, 11):
    input_num = int(input("숫자를 입력해주세요: "))
    input_nums.append(input_num)
    if (input_num > ran_num):
        print("down")
    elif (input_num < ran_num):
        print("up")    
    else:
        print("{}는 정답입니다".format(ran_num))
        print("오답횟수: {}".format(num - 1))
        break
print("입력한 숫자: {}".format(input_nums))
print("입력한 횟수: {}".format(num))
print("정답: {}".format(ran_num))
