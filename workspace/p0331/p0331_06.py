# student_info = [1, "홍길동", 100, 100, 100, 300, 100.0, 0]

# students_info = [[1, "홍길동", 100, 100, 100, 300, 100.0, 0], 
#                  [2, "이순신", 100, 100, 100, 300, 100.0, 0], 
#                  [3, "유관순", 100, 100, 100, 300, 100.0, 0]]

# print("                    학생 성적 프로그램")
# print("-"*60)
# print("번호\t이름\t국어\t수학\t영어\t합계\t평균\t등수")
# for infos in students_info:
#     for si in infos:
#         print(si, end='\t')
#     print()

students = list()
student = []

while True:
	students = list()
	no = 1
	name = input("이름을 입력하세요: ")
	kor = int(input("국어 점수를 입력하세요: "))
	eng = int(input("영어 점수를 입력하세요: "))
	mat = int(input("수학 점수를 입력하세요: "))

	sum_score = kor + eng + mat
	avr_score = sum_score / 3
	rank = 0
	student = [no, name, kor, eng, mat, sum_score, avr_score, rank]
	students.append(student)

	print("                    학생 성적 프로그램")
	print("-"*60)
	print("번호\t이름\t국어\t수학\t영어\t합계\t평균\t등수")
	for stu in students:
		for i, s in enumerate(stu):
			if (i != 6):
				print(s, end = "\t")
			else:
				print("{:.2f}".format(s))		
		print()

