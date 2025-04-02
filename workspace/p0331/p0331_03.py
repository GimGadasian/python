# # i = 0
# # while (i < 10):
# #     print(i, end=" ")
# #     i += 1   
# # print()

# # i = 0
# # for i in range(10):
# #     print(i, end=" ")
   
# # list 생성 
# # nums = []
# # i = 0
# # sum_num = 0
# # n = 0

# # for i in range(10):
# #     num = int(input("숫자를 입력하세요: "))
# #     nums.append(num)

# # # for 구문으로 요소 총합 구하기
# # for n in nums:
# #     sum_num += n
# # print("list: {}, sum: {}".format(nums, sum_num))

# # sum_num = 0
# # i = 0 
# # # while 구문으로 요소 총합 구하기    
# # while (i < 10):
# #     sum_num += nums[i]
# #     i += 1
# # print("list: {}, sum: {}".format(nums, sum_num))

# # lottery program

# # lotto = []
# # my_input = []
# # i = 0
# # j = 0
# # input_num = 0
# # my_lotto = []

# # import random

# # lotto = random.sample(range(1, 100), 6)

# # while (i < 6):
# #     input_num = int(input("숫자를 입력하세요: "))
# #     if (input_num not in my_input):    
# #         my_input.append(input_num)
# #         i += 1
# # print(lotto)
# # print(my_input)

# # while (j < 6):
# #     if (lotto[j] in my_input):
# #         my_lotto.append(lotto[j])
# #     j += 1
# # print(my_lotto)


# # a_list = [i+1 for i in range(45)]
# # random.shuffle(a_list)
# # print(a_list[:6])
   
# # print(int(random.random()*10)+1) 

# # nums = [i+1 for i in range(100)]
# # num = 0

# # # sum of nums
# # sum_odd = 0
# # sum_even = 0
# # sum = 0

# # for num in nums:
# #     if (num % 2 == 0): # even
# #         sum_even += num
# #     else: # odd
# #         sum_odd += num

# # print(sum_odd)
# # print(sum_even)


# # for i in range(100):
# #     sum += i
# #     if (sum > 200):
# #         break
# # print("넘어가는 항:", i)
# # print("합:", sum)

# # print("직전 항:", i-1)
# # print("합:", sum - i)


# # continue, break, pass
# # continue: 조건 해당 시 실행 중지
# # break: 조건 해당 시 프로그램 종료
# # pass: 조건 해당해도 실행
# input_sum = 0

# while True:
#     input_num = int(input("숫자를 입력하세요: ")) 
#     if (input_num % 5 == 0):
#         print("5의 배수 입력 금지!")
#         continue
#     input_sum += input_num
#     if (input_sum > 50):
#         break
# print(input_sum)
 
# input_sum = 0   
# while (input_sum < 50):
#     input_num = int(input("숫자를 입력하세요: ")) 
#     if (input_num % 5 == 0):
#         print("5의 배수 입력 금지!")
#         continue
#     input_sum += input_num    
# print(input_sum)

# # 문자열 입력 시 예외 처리
# input_sum = 0   
# while (input_sum < 50):
#     try:
#         input_num = int(input("숫자를 입력하세요: ")) 
#         if (input_num % 5 == 0):
#             print("5의 배수 입력 금지!")
#             continue
#         input_sum += input_num
#     except ValueError:
#         print("숫자를 입력하세요!")
    
# print(input_sum)
        
# list_origin = [1, 2, 3, 4]        
# list_swap =list_origin[::-1]
# list_edit = [*list_origin]

# list_edit[1:2] = [100, 500] 

# print(list_origin)
# print(list_swap)
# print(list_edit)

# # 2차원 list

# list_wh = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

# print(list_wh)    

# i = 0
# j = 0

# for i in range(3):
#     for j in range(3):
#         print(list_wh[i][j], end="  ")
#     print()
    
# print()

k = 0
l = 0

list_5b5 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
    ]

for k in range(5):
    for l in range(5):
        print("{:2d}".format(list_5b5[k][l]), end="\t")
    print()
    print()

print()
import random
i = 0
j = 0
k = 0
m = 0
n = 0

list_5x5 = [[0]*5 for i in range(5)] # deep copy / [[0]*5]*5 shallow copy

sample_list = [i+1 for i in range(25)]
random.shuffle(sample_list)

for j in range(5):
    for k in range(5):
        list_5x5[j][k] = sample_list[5*j + k]

for m in range(5):
    for n in range(5):
        print("{:2d}".format(list_5x5[m][n]), end ="\t")
    print()
    print()

# 초기화 방법 2
# list_innit = list()
# for i in range(5):
#     temp = []
#     for j in range(5):
#         temp.append(0)
#     sample_list.append(temp)
# print(sample_list)