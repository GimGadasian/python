x_val = int(input("x 값: "))
y_val = int(input("y 값: "))
xy_list =[]

print("({}, {})".format(x_val, y_val))

xy_list.append(x_val)
xy_list.append(y_val)

print(xy_list)

# split

name = input("성: , 이름: ")
name_lst = name.split(",")
print(name_lst)