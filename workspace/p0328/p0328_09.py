for i in range(1, 100):
    print("{:03d}".format(i))
    
# 구구단 출력 프로그램

i = 0
j = 0
k = 0 
l = 0

for j in range(1, 9+1):
    for i in range(2, 9+1):
        print("{} * {} = {:2d}\t".format(i, j, i*j), end="")
    print()

print()
   
for k in range(2, 9+1):
    for l in range(1, 9+1):
        print("{} * {} = {:2d}\t".format(k, l, k*l), end="")
    print()