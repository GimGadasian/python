students = [
    {"no" : 1, "name" : "a", "kor" : 100 , "eng" : 100, "mat" : 100 , "sum" : 300, "avr" : 100, "rank" : 0},
	{"no" : 1, "name" : "a", "kor" : 100 , "eng" : 100, "mat" : 100 , "sum" : 300, "avr" : 100, "rank" : 0},
	{"no" : 1, "name" : "a", "kor" : 100 , "eng" : 100, "mat" : 100 , "sum" : 300, "avr" : 100, "rank" : 0}
]

count = 4 # 학생 번호
title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

while True:
    print("-" * 40)
    print("---< 학생 성적 입력 프로그램 >---")
    print("-" * 40)
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 학생 성적 삭제")
    print("0. 프로그램 종료")
    print("-" * 40)
    choice = int(input("번호 입력: "))
    if (choice == 1):
        print("--< 학생 성적 입력 시작 >--")
        no = count
        name = input("학생 이름 입력 / 0. 이전 화면으로: ")
        if (name == "0"):
            continue
        kor = int(input("국어 점수 입력:"))
        eng = int(input("영어 점수 입력:"))
        mat = int(input("수학 점수 입력:"))
        sum_score = kor + eng + mat
        avr_score = sum_score / 3
        rank = 0
        
        students.append({"no" : count, "name" : name, "kor" : kor, "eng" : eng, "mat" : mat , "sum" : sum_score, "avr" : avr_score, "rank" : rank})
    
    elif (choice == 2): 
        print("--< 학생 성적 현황 >--")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print()
        for st in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(st["no"], st["name"], st["kor"], st["eng"], st["mat"], st["sum"], st["avr"], st["rank"]))
    
    elif (choice == 3): 
        print("--< 학생 성적 수정 시작 >--")
        name = input("성적을 수정하고자 학생 이름: ")
        
        temp = 0
        
        for i, s in enumerate(students):
            if (name in s):		
                print()
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 수정 안 함")
                print()
                choice = int(input("번호를 입력하세요: "))
            else:
                print("해당 학생 미존재")
            
    
    elif (choice == 4): 
        pass
    
    else:
        print("프로그램 종료")
        break

