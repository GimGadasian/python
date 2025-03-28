# 파이썬 타입
# bool 타입
if True:
    print("true")
    
if (10 > 3):
    print("it's true")

print(10 < 3)
print(1 + 2)
print("1" + "2")

print("{}".format(1 + 2))

int_str = "1"
print(int(int_str) + 1) # 숫자 형태 문자열만 변경 가능

print(int(1.5)) # 소숫점 없어짐
print(float(1)) # 소숫점 생김
# print(int("1.5")) error

print(type(str(1.5)))

# 리스트
list_alpha = ["a", "b", "c", "d"]
print(list_alpha)
print(list_alpha[0] + list_alpha[1])

# score = input("데이터를 입력하세요: ")

# print("입력 데이터:", score)

#  두 수를 입력 받아 합계, 평균 구하는 프로그램

num1 = int(input("입력하세요: "))
num2 = int(input("입력하세요: "))
sum_num = num1 + num2
avr_num = sum_num / 2
print("합계: {}, 평균: {}".format(sum_num, avr_num))
print()

score = int(input("점수를 입력하세요: "))
if (score > 90):
    if (score >= 95):
        print("A", end="")
        print("+")
        print(":)")
    else: pass
else:
    print(":(")
    
    