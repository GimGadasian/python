a = 10
b = 11
c = 10
d = 20
e = 30
f = 1

print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=d)
# 관계 연산자는 True, False로 결과를 반환

# 논리 연산자 and, or, not
print((a==b) and (a==c)) # False and True = False
print((a==b) or (a==c)) # False or True = True
print(not(d==f)) # not False = True

# 비트 연산자 &, |, ^, ~, <<, >>
print(a & b) # 1010 & 1011 = 1010
print(a | b) # 1010 | 1011 = 1011
print(a ^ b) # 1010 ^ 1011 = 0011
print(~a) # ~1010 = 0101
print(a << 1) # 1010 << 1 = 10100
print(a >> 1) # 1010 >> 1 = 101

# 조건문 if, elif, else
num1 = 10
num2 = 100
if (num1 < num2):
    print("num1이 num2보다 작다.")
    
print("다음 구문 실행") # 조건문 밖을 나와야 실행된다

# 양수인지 음수인지 판별하는 프로그램
input_num = int(input("숫자를 입력하세요: "))
if (input_num > 0): # True
    print("{}는 양수입니다\n".format(input_num))
else: # False
    print("{}는 음수입니다\n".format(input_num))

# 짝수인지 홀수인지 판별하는 프로그램
input_num = int(input("숫자를 입력하세요: "))
if (input_num % 2 == 0):
    print("{}는 짝수입니다\n".format(input_num))
else:
    print("{}는 홀수입니다\n".format(input_num))

# 3의 배수인지 판별하는 프로그램
input_num = int(input("숫자를 입력하세요: "))
if ( input_num %3 == 0):
    print("{}는 3의 배수입니다\n".format(input_num))
else:
    print("{}는 3의 배수가 아닙니다\n".format(input_num))
