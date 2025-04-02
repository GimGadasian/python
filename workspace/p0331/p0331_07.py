# 초기화

count = 1
students = list() # 다차원 리스트 생성 함수
title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]
kor = 0
eng = 0
mat = 0
no = 0
name = ''
rank = 0


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
    
    # 번호 입력 받기
    choice = int(input("원하는 번호를 입력하세요: "))     
    
    # 번호에 대응하는 프로그램 실행
    if (choice == 1):
        print("학생 성적 입력")
        
        no = count    
        name = input("이름을 입력하세요: ")
        kor = int(input("국어 점수를 입력하세요: "))
        eng = int(input("영어 점수를 입력하세요: "))
        mat = int(input("수학 점수를 입력하세요: ")) 
        sum_score = kor + eng + mat
        avr_score = sum_score / 3
        rank = 0
        count +=1
        students.append([no,name,kor,eng,mat,sum_score,avr_score,rank])
        
        print("{}번 {} 학생 성적 등록 완료\n".format(no, name))
        
    
    elif (choice == 2):
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        for student in students:
            print("{:2d}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{:2d}".format(*student))
            
        
    elif (choice == 3):
        print("학생 성적 수정")
        name = input("수정하고자 하는 학생 이름을 입력하세요: ")
        for i, s in enumerate(students):
            temp = 0
            if (name in s):
                print("{} 학생".format(name))
                print()
                print("수정하고자 하는 과목 선택: ")
                print("1, 국어")
                print("2, 영어")
                print("3, 수학")
                print("0, 수정 취소")
                print()
                choice = int(input("번호 입력: "))
                if (choice == 1):
                    print("국어 점수 수정")
                    print("현재 국어 점수: {}".format(s[2]))
                    s[2] = int(input("변경 국어 점수: "))
                    # 합계
                    # 평균
                    print("수정하였습니다")
                
                elif (choice == 2):
                    print("영어 점수 수정")
                    print("현재 영어 점수: {}".format(s[2]))
                    s[3] = int(input("변경 영어 점수: "))
                    s[5] = s[2] + s[3] + s[5]
                    s[6] = s[5] / 3
                    print("수정하였습니다")
                
                else:
                    print("수학 점수 수정")
                    print("현재 수학 점수: {}".format(s[2]))
                    s[4] = int(input("변경 수학 점수: "))
                    s[5] = s[2] + s[3] + s[5]
                    s[6] = s[5] / 3
                    print("수정하였습니다")
                
            if (temp == 0):
                print("목록에 없는 학생")
        
    elif (choice == 4):
        print("학생 성적 삭제")
        name = input("삭제하고자 하는 학생 이름을 입력하세요: ")
        for i, s in enumerate(students):
            temp = 0
            if (name in s):
                temp = 1
                print("{} 학생".format(name))
                choice = int(input("삭제하시겠습니까?(예: 1 / 아니오: 0) "))
                if (choice == 1):
                    print("삭제")
                    del students[i]
                else:
                    print("수정 사항 없음")
                
            else:
                print("목록에 없는 학생")
                break               
            if (temp) == 0:
                break
            
    elif (choice == 5):
        print("학생 성적 검색")
    elif (choice == 6):
        print("프로그램 종료")
    else:
        print("프로그램 종료")
        break
    