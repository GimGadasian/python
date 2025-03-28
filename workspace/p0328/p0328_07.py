# # while 문: 조건문에 해당될 때 반복 / 조건식이 맞으면 무한 반복 가능

# i = 0
# j = 0

# while (i < 10): # 조건에 맞춰 반복 
#     i += 1
#     print(i)
    
# for j in range(1, 10+1): # 횟수에 맞춰 반복
#     print(j)

input_list = []
i = 0
j = 0

while (i < 10):
    j += 1
    input_num = input("숫자를 입력하세요(attempt{}): ".format(j))    
    if (input_num not in input_list):
        input_list.append(input_num)
        i += 1
            
print(input_list)


