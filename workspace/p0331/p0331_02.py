a_list = [1, 2, 3, 4, 5]
for i, value in enumerate(a_list):
    print(f"{i} : {value}")
    
# append 추가
i = 0
app_list = []
for i in range(1, 10+1):
    app_list.append(i)
print(app_list)


# list 내포
i = 0
fast_list = [i for i in range(1, 10+1)]
print(fast_list)

# 다양한 리스트 추가/삭제 함수들
fast_list.insert(0, 100)
print(fast_list)

fast_list.extend(app_list)
print(fast_list)

del fast_list[1] # 인덱스에 해당하는 값 삭제
print(fast_list)

fast_list.pop() # 맨 뒤 삭제 
print(fast_list)

fast_list.remove(1) # 값 삭제
print(fast_list)

fast_list.clear()
print(fast_list)




# var_list = [0, 0.1, "김", "a"]
# print(var_list)