import random

# 1차원 리스트
list_1 = [i for i in range(1, 25+1)] # == (i+1) for i in range(25)
print(list_1)
print()

random.shuffle(list_1) # random.random(), random.randint(), random.sample(), random.shuffle()...
print(list_1)
print()

# 2차원 리스트

# 초기화(25, 1차원)
list_2_innit = [[0]*5 for i in range(5)] 
print(list_2_innit)
print()

# 랜덤 1차원 리스트 값 넣어주기
for i in range(5):
    for j in range(5):
        list_2_innit[i][j] = list_1[(5*i) + j]

new_list_2 = list_2_innit 
print(new_list_2)
print()

while True:
    # 2차원(5 x 5)로 출력
	print("\t0\t1\t2\t3\t4\t")
	print("-" * 45)
 
	for i in range(5):
		print("{}  |".format(i), end="\t")
		for j in range(5):
			print(new_list_2[i][j], end ="\t")	
		print()
		print()
		print()
	
 # 좌표 입력 방식
	x_val = int(input("input the x value: "))
	y_val = int(input("input the y value: "))
 
 # 번호 입력 방식
	# stop = 0
	# input_num = int(input("input the number: "))
	# for i in range(5):
	#	for j in range(5):
	# 		if (new_list_2[i][j] == input_num):
	#			new_list_2[i][j] = ":)"
	#           stop = 1
	#			break  // 비교하는 반복이 굳이 더 돌아갈 필요가 없다!
	#		if (stop = 1):
	#       	break
	new_list_2[y_val][x_val] = ":)"
	
	count = 0
 
	
			
	
 

    	
      


