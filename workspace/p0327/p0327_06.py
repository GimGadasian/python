num = 7
if (0 <= num <= 10):
    print("1의 자리 숫자입니다")

# 다른 언어
# if (0 <= num && num <= 10)
#     printf("1의 자리 숫자입니다")

# 사계절 판별 프로그램
# 봄(3~5), 여름(6~8), 가을(9~11), 겨울(12, 1, 2)
month = int(input("월을 입력하세요: "))
if (3 <= month <= 5): 
    print("봄입니다")
elif (6 <= month <= 8):
    print("여름입니다")
elif (9 <= month <= 11):
    print("가을입니다")
else:
    print("겨울입니다")