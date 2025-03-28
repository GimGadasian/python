import random
# 0보다 같거나 크고, 1미만인 랜덤 실수 값을 뽑아서 전달해줌, (0 =< x < 1)

# 랜덤 숫자를 맞추는 프로그램

# # 1~100 까지의 숫자를 입력받음

# 반복문
ran_num = random.randint(1, 100)
input_nums = []
for num in range(1, 11):
    try:
        input_num = int(input("숫자를 입력해주세요 (1~100): "))
        if input_num < 1 or input_num > 100:
            print("1에서 100 사이의 숫자를 입력해주세요.")
            continue
        input_nums.append(input_num)
        if ran_num == input_num:
            print("정답입니다, 랜덤숫자: {}".format(ran_num))
            break
        elif ran_num < input_num:
            print("down")
        elif ran_num > input_num:
            print("up")
    except ValueError:
        print("유효한 숫자를 입력해주세요.")
        continue

print("랜덤 숫자: {}".format(ran_num))
print("도전횟수: {}".format(len(input_nums)))
print("입력된 숫자: {}".format(input_nums))

