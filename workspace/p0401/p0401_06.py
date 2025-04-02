dic = {1 : "a", 2 : "b", 3 : "c"}
print(dic)

student_info = {"학번" : 20224097, "이름" : "김가은", "학과" : "소프트웨어"}
print(student_info)

stud_info = {}
stud_info["no"] = 1
stud_info["name"] = "Tom"
print(stud_info)

stud_info["name"] = "Party Anthem"
print(stud_info)

print(stud_info.get("name"))
print(stud_info.keys())
print(stud_info.values())
print(stud_info)

for i, value in enumerate(stud_info):
    print("{} : {}".format(i, value))

for key in stud_info:
    print(stud_info[key])

