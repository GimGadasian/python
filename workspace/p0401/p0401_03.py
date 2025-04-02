students = list()
student = []

count = 1
students = list() # 다차원 리스트 생성 함수
title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

# while 구문 안에 번호 입력 프로그램 넣기
while True:
    # 화면 출력
	print(" "* 5, end="")
	print("< 학생성적 프로그램>")
	print("-"*30)
	print("1. 학생 성적 입력")
	print("2. 학생 성적 출력")
	print("3. 학생 성적 수정")
	print("4. 학생 성적 삭제")
	print("5. 학생 성적 정렬")
	print("6. 학생 성적 검색")
	print("7. 학생 등수 처리")
	print("0. 프로그램 종료")

	print("-"*30)
        
	# 번호에 대응하는 입력 받기
	choice = int(input("번호 입력: "))
	if (choice == 1):
		print("---<학생 성적 입력 시작>---")
		name = input("성적을 입력하고자 하는 학생 이름: ")
		no = count
		kor = int(input("국어: "))
		eng = int(input("영어: "))
		mat = int(input("수학: "))
		sum_score = kor + eng + mat
		avr_score = sum_score / 3
		rank = 0
		count +=1
		students.append([no, name, kor, eng, mat, sum_score, avr_score, rank])

	elif (choice == 2):
		print("---<학생 성적 모음>---")
		print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
  
		for student in students:
			
			print("{:2d}\t{}\t{:2d}\t{:2d}\t{:2d}\t{}\t{:.2f}".format(*student))
  
	elif (choice == 3):
		print("--<학생 성적 수정 시작>--")
		name = input("성적을 수정하고자 학생 이름: ")
		temp = 0
		print("{} 학생의 수정하고자 하는 과목".format(name))
  
		for i, s in  enumerate(students): #  i == index , s == element
			temp = 1
			if (name in s):		
				print()
				print("1. 국어")
				print("2. 영어")
				print("3. 수학")
				print("0. 수정 안 함")
				print()
				choice = int(input("번호를 입력하세요: "))
    
				if (choice == 1):
					s[2] = int(input("점수 입력: ")) # 국어 점수 수정
					s[5] = s[2] + s[3] + s[4]
					s[6] = s[5] / 3
					
     
				elif (choice == 2):
					s[3] = int(input("점수 입력: ")) # 영어 점수 수정
					s[5] = s[2] + s[3] + s[4]
					s[6] = s[5] / 3
     
				elif (choice == 3):
					s[4] = int(input("점수 입력: ")) # 수학 점수 수정
					s[5] = s[2] + s[3] + s[4]
					s[6] = s[5] / 3
     
				else:
					print("수정 사항 없음")
					break
			
			if (temp == 0):
				print("목록에 없는 학생")
    	

			
    


	elif (choice == 4):
		pass

	elif (choice == 5):
		pass

	elif (choice == 6):
		pass

	elif (choice == 7):
		pass

	else:
		pass


	