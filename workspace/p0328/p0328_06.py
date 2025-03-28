# 숫자 맞추기

import random
lotto_num = random.randint(1, 45) 
input_list = []

for i in range(10):

    input_num = int(input("숫자를 입력하세요(attempt.{}) >>".format(i+1)))
    input_list.append(input_num)

    if (input_num == lotto_num):
        print("당첨입니다")
        break
    else:
        print("틀렸습니다", end="")
        if (input_num > lotto_num):
            print("down")
        else:
            print(" up")
    
print("랜덤번호: {}".format(lotto_num))
print("도전횟수: {}".format(i+1))
print("입력 목록: {}".format(input_list))
