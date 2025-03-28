# 1에서 100사이의 홀수만 숫자를 더해서 합계를 구하시오
sum = 0
for i in range(1, 100+1, 2):
    sum += i
print("합계: {}".format(sum))

# 3의 배수만 더해서 합 구하기

sum = 0
for j in range(1, 100):
    if ((j % 3 == 0) and (j % 5 == 0)):
        sum += j
print("합계: {}".format(sum))

sum = 0
for k in range(1, 100):
    if((k % 3 == 0) or (k % 7 == 0)):
        sum += k
print("합: {}".format(sum))

