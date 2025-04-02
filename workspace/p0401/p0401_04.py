list_1 = [1, 2, 3, 4]

del list_1[0]
list_1.pop()
list_1.remove(2)
list_1.clear()

print(len(list_1))

count = 0

lists = [1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 6, 1]
for l in lists:
    if (l == 1):
        count += 1
print("{} : {}개".format(1, count))
        
# 순차 정렬 / 역순 정렬
lists_up = list.sort()
lists_down = lists.reverse()
print(lists_up)
print(lists_down)

