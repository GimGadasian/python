num_list = [111, 112, 113, 1, 2, 3, 211]

new_list = []
sum_num = 0
for num in num_list:
    if (num > 100):
        new_list.append(num)

for n in new_list:
    sum_num += n
    
print(new_list)
print(sum_num)
        
# 리스트 속 요소들의 자릿수 구하기

size_list = []
for num in num_list:
    size_list.append(len(str(num)))
    
print(size_list)

