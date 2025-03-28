# 날짜 시간
# 날짜 클래스
import datetime

now = datetime.datetime.now()  # Fix: Call the method to get the current datetime instance
print("현재 시간: ", now)

print("현재 연도: ", now.year)  # Fix: Remove parentheses
print("현재 월: ", now.month)  # Fix: Remove parentheses
print("현재 일: ", now.day)  # Fix: Remove parentheses
    
print("{}-{}-{}".format(now.year, now.month, now.day))  

# 시간이 12시 이후면 오후, 이전이면 오전이라고 출력
hour = now.hour
min = now.minute
if (hour >= 12):
    print("{:02d}:{:02d}PM".format((hour - 12), min))
else:
    print("{:02d}:{:02d}AM".format(hour, min))