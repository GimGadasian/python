# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# arr1 = [i+1 for i in range(100)] # 리스트 내포 ****************

# print(arr1)

i = 0
a_list = [1, 2, 3]
aa_list = ["1m", "2m", "3m"]
aaa_list = [str(i) + "m" for i in a_list]
print(aaa_list)

list_org = [i+1 for i in range(100)]

list_100 = [i+100 for i in list_org]
print(list_100)

# 기존 방식
list_vac = []
for i in range(100):
    list_vac.append(i+1)
print(list_vac)

