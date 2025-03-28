# # 두 수를 입력 받아, 두 수 사이의 합계를 구하시오

# num1 = int(input("숫자를 입력하세요: "))
# num2 = int(input("숫자를 입력하세요: "))

# print(num1, num2)

# sum = 0
# t = 0
# if (num1 > num2):
#     t= num1
#     num1 = num2
#     num2 = t
    
# for i in range(num1, num2 + 1):
#      sum += i
    
# print("{} + {} + ... + {} +{} = {}".format(num1, num1+1, num2-1, num2, sum))

# 구구단 for문 두 번
# for i in range(2, 9+1):
#     if (i%2 == 0):
#         print("< {}단 >\n".format(i))
#         for j in range(1, 9+1):
#             print("{} * {} = {}".format(i, j, i*j), end="")
#         print()
#         print()

i = 0
j = 0
vacant = 0


num_first = int(input("첫 번째 숫자를 입력하세요: "))
num_second = int(input("두 번째 숫자를 입력하세요: "))

if (num_first > num_second):
    vacant = num_first
    num_first = num_second
    num_second = vacant

for i in range(num_first, num_second+1):
    print("< {} > 단\n".format(i))
    for j in range(num_first, num_second+1):
        print("{} * {} = {}".format(i, j, i*j), end="")
        print()
        print()