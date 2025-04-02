list_1 = [[1, 2, "x", 4,"x"], [2, 3, "x", 5, 0]]

count = 0

for i in range(5):
    if list_1 [0][i] == "x":
        count += 1
        
if count == 2:
    print(":)")