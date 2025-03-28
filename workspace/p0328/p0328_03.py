# # 반복문을 활용해서 1~10 출력
# for i in range(1, 11):
#     print(i)
# print()
    
# a = 10
# if (a < 5 and a < 9):
#     print(a)
# if (a > 5 or a > 9):
#     print(a)
    
# print()
# # 문자 선택 연산자 / 문자열: 문자들을 모아 놓아 만든 열 -> 리스트와 유사하게 인식

# hello = "안녕하세요"
# for hi in hello:
#     print(hi)
# for hi in hello:
#     print(hi, end="")
# print()
# print()    
    
# # 슬라이싱
# print(hello[1:4])
# print(hello[0:5])
# print(hello[::2])
# print(hello[0:5:2])
# print(hello[::-1])
# print(hello[:-1]) # (0, 1, 2, 3, 4) = (-5, -3, -3, -2, -1)

# print(len(hello))
# print(hello[1:len(hello)+1])

# for i in range(1, 11, 2): 
#     print(i, end="")

sum = 0
for i in range(1, 100+1):
    sum += i
    if (sum > 100):
        break
print("위치: {}번 값: {}".format(i, sum))

# 1+2+... 에서 값이 처음으로 100 이상이 되는 위치와 그 값

