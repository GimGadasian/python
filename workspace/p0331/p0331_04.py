import random

# 1~25 랜덤 정수로 채운 1차원 리스트 생성
sample_list = [i+1 for i in range(25)]
random.shuffle(sample_list)

# 0으로 초기화 된 1차원 리스트 생성
list_5x5_innit = [[0]*5 for i in range(5)]

# 초기화 된 값에 랜덤 리스트 값 넣기
for i in range(5):
    for j in range(5):
        list_5x5_innit[i][j] = sample_list[(5*i)+j]
        
new_list = list_5x5_innit
        
print(new_list)

print()
while True: 
	# 2차원 리스트 형태로 출력 / X, Y 좌표 그리기
	print("\t0\t1\t2\t3\t4\t")
	print("-" * 40)

	for i in range(5):
		print("{}  |".format(i), end="\t")
		for j in range(5):
			print(new_list[i][j], end='\t')
		print()
		print()
		print()

	x_val = int(input("x 값을 입력하세요: "))
	if (x_val > 4 or x_val < 0):
		continue
	if (type(x_val) != int):
		continue
	y_val = int(input("y 값을 입력하세요: "))
	if (y_val > 4 or x_val < 0):
		continue
	if (type(y_val != int)):
		continue

	new_list[y_val][x_val] = ":)"
	
 