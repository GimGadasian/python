import random


ran_list = random.sample(range(1, 45), 7)
my_list = []
ran = 0
i = 0
j = 0
k = 0
l = 0
lotto_count = 0
lotto_list = []
while (i < 10):
    input_num = int(input("숫자 입력(append.{}): ".format(j+1)))      
    if (input_num not in my_list):    
        my_list.append(input_num)  
        i += 1
    j += 1
    
print("랜덤 번호: {}".format(ran_list))
print("입력번호: {}".format(my_list))

for k in range(7):
    for l in range(10):
        if(ran_list[k] == my_list[l]):
            lotto_count += 1
            lotto_list.append(my_list[l])
            break
print("본인 당첨번호 리스트: {}".format(lotto_list))