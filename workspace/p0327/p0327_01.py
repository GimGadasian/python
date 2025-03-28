# a = 20
# num = 30

# print("a: %d" % a)
# print("num: {}".format(num))

# # 입력 input -> 자료형 str -> int로 변환
# num1 = input("숫자를 입력하세요: ") # 문자열
# num2 = input("숫자를 입력하세요: ")
# print("입력된 숫자: {}, {} / str합계: {} / int 합게: {}".format(num1, num2, num1 + num2, int(num1) + int(num2)))

# 성적 입력 프로그램
# 이름, 국어, 영어, 수학 입력 -> 총점, 평균 출력 프로그램

print("*" * 50)
print("성적 입력 프로그램")
print("*" * 50)
name = input("이름을 입력하세요: ")
score_kor = int(input("국어 점수를 입력하세요: "))
score_eng = int(input("영어 점수를 입력하세요: "))
score_mat = int(input("수학 점수를 입력하세요: "))
sum_score = score_kor + score_eng + score_mat
avr_score = sum_score / 3
print()
print("이름\t국어\t영어\t수학\t총점\t평균")
print("-" * 50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name, score_kor, score_eng, score_mat, sum_score, avr_score))

# 문자형 숫자는 정수, 실수형으로 변환 가능
a_str = "100"
b_str = "200"
print(a_str, type(a_str))
print(b_str, type(b_str))
int_a = int(a_str)
int_b = int(b_str)
print(int_a, type(int_a))
print(int_b, type(int_b))

# 약식 연산 기호
a = 0
a += 10
print(a)
a -= 5  
print(a)
a *= 2
print(a)
a //= 3
print(a)
a %= 2
print(a)