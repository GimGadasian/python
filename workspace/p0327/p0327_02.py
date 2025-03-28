# 달러를 입력하면, 원화 환산 출력 프로그램
# 1달러는 1467원

# 달러 입력
dollar = int(input("달러를 입력하세요: "))
won = dollar * 1467
# 쉼표가 천원 단위로 구분
print("달러: {:,d}$".format(dollar))
print("원화: {:,d}원".format(won))

# 동전 변환 프로그램
# 500원, 100원, 50원, 10원, 1원
origin = won
coins_500 = origin // 500
coins_100 = (origin % 500) // 100
coins_50 = (origin % 100) // 50
coins_10 = (origin % 50) // 10
coins_1 = (origin % 10) // 1
print("500원: {}개".format(coins_500))
print("100원: {}개".format(coins_100))
print("50원: {}개".format(coins_50))
print("10원: {}개".format(coins_10))
print("1원: {}개\n".format(coins_1))

# 반지름을 입력받아 원의 넓이와 둘레를 구하는 프로그램

radius = float(input("반지름을 입력하세요: "))
pi = 3.141592
circle_area = pi * (radius ** 2)
circle_length = 2 * pi * radius
print("원의 넓이: {:.2f}m2".format(circle_area))
print("원의 둘레: {:.2f}m".format(circle_length))

# 사각형의 가로 세로 값을 입력 받아 넓이와 둘레 구하는 프로그램
width = float(input("가로를 입력하세요: "))
height = float(input("세로를 입력하세요:"))
rec_area = width * height
rec_length = 2 * (width + height)
print("사각형 넓이: {:.2f}m2".format(rec_area))
print("사각형 둘레: {:.2f}m".format(rec_length))

# 삼각형의 밑변과 높이를 입력 받아 넓이를 구하는 프로그램
base = float(input("밑변을 입력하세요: "))
height = float(input("높이를 입력하세요: "))
tri_area = 0.5 * base * height

# 관계 연산자
# >, <, >=, <=, ==, !=      