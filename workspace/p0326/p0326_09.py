name = input("이름: ")
score1 = input("국어: ")
score2 = input("수학: ")
sum_score = int(score1) + int(score2)
avr_score = sum_score / 2

print("이름: ", name)
print("국어: ", score1)
print("수학: ", score2) 
print("합계: ", sum_score)
print("평균: %.1f" % avr_score)