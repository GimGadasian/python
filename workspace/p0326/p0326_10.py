# 숫자 두 개 입력, 사칙 연산 결과 출력
# 1. 두 수 입력
num1 = int(input("첫 번째 수 입력:"))
num2 = int(input("두 번째 수 입력:"))
# 2. 덧셈
str_add = "{} + {} = {}".format(num1, num2, num1 + num2)
#3. 뺄셈
str_suv = "{} - {} = {}".format(num1, num2, num1 - num2)
#4. 곱셈    
str_mult = "{} * {} = {}".format(num1, num2, num1 * num2)
#5. 나눗셈
str_div = "{} / {} = {:.0f}".format(num1, num2, num1 / num2)
#6. 출력
print(str_add)
print(str_suv)
print(str_mult)
print(str_div)

#국영수 점수 입력, 합계, 평균 출력
# 1. 국영수 점수 입력
score_kor = int(input("국어 점수 입력:"))
score_eng = int(input("영어 점수 입력:"))
score_math = int(input("수학 점수 입력:"))
# 2. 합계
sum_score = score_kor + score_eng + score_math
# 3. 평균
avr_score = sum_score / 3
# 3. 출력
print("합계: {}\n평균: {:.2f}".format(sum_score, avr_score))
# str_sum_score = "합계: {}".format(sum_score)
# str_avr_score = "평균: {:.2f}".format(avr_score)
# print(str_sum_score)
# print(str_avr_score)
