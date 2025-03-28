name = input("이름을 입력하세요: ")

score_kor = int(input("국어 점수를 입력하세요: "))
score_eng = int(input("영어 점수를 입력하세요: "))
score_mat = int(input("수학 점수를 입력하세요: "))

sum_score = score_kor + score_eng + score_mat
avr_score = sum_score / 3

print("*" * 50)
print("성적 입력 프로그램")
print("*" * 50)
print("이름\t국어\t영어\t수학\t총점\t평균")
print("*" * 50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name, score_kor, score_eng, score_mat, sum_score, avr_score))
print("*" * 50)
