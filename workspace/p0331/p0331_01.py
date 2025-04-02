# # 구구단
# for i in range(2, 9+1):
#     for j in range(1, 9+1):
        
#         print("{} * {} = {:2d}".format(i, j, i*j))
#     print()

# nums = [1, 2, 3, 4, 5]
# num = 0
# sum_num = 0
# for num in nums:
#     sum_num += num
# print(sum_num)

# shallow copy: 주소 복사
a_list = [1, 2, 3, 4, 5]
a = 10

a_list[0] = 100

print("a: ", a)
print("a_list:", a_list)

b = a 
b_list = []
b = 1000
print("b:", b)

b_list = a_list
print("b_list:", b_list)
b_list[0] = 200

print("a_list:", a_list)
print("b_list:", b_list)

# deep copy
c_list = [1, 2, 3, 4, 5]
d_list = [*c_list]

d_list[0] = 10

print("c_list:", c_list)
print("d_list:", d_list)
