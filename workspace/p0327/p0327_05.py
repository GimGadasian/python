# # # 서너가지의 조건이 필요할 땐?

# # # 정수의 음양 판별 조건문
# # num = 0
# # if (num > 0):
# #     print("양수")
# # elif (num < 0):
# #     print("음수")
# # else: 
# #     print("0")
    
# # # 시험 성적 입력, 60점 이상 합격, 미만 불합격
# # score = int(input("시험 점수를 입력하세요: "))
# # if (score >= 60):
# #     print("합격")   
# # else:
# #     print("불합격")    

# # 70점 이상 합격, 69~60점 재시험, 미만 불합격
# score = int(input("시험 점수를 입력하세요: "))
# if (score >= 70):
#     print("합격")
# elif (score >= 60):
#     print("재시험")
# else:
#     print("불합격") 


# 시험 90 점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, 미만 F
# 세부성적 +, -

score = int(input("시험 점수를 입력하세요: "))
if (score >= 90):
    print("A", end="")
    if (score >= 97):
        print("+")
    elif (score >= 93):
        pass
    else: 
        print("-")
elif (score >= 80):
    print("B", end="")
    if (score >= 87):
        print("+")
    elif (score >= 83):
        pass
    else:
        print("-")
elif (score >= 70):
    print("C", end="")
    if (score >= 77):
        print("+")
    elif (score >= 73):
        pass
    else:
        print("-")
elif (score >= 60):
    print("D", end="")
    if (score >= 67):
        print("+")
    elif (score >= 63):
        pass
    else:
        print("-")
else:
    print("F")
    
print()
print("안녕", end="")
print("하세요") # end=""는 줄바꿈을 하지 않는다
