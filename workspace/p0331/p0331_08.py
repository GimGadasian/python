import random

random_list = [i+1 for i in range(25)]
random.shuffle(random_list)

list_init_5x5 = [[0]*5 for i in range(5)]


for i in range(5):
    for j in range(5):
        list_init_5x5[i][j] = random_list[(5*i)+j]
new_list = list_init_5x5


while True:
    print("-"*40)
    for i in range(5):
        for j in range(5):
            print(new_list[i][j], end="\t")
        print()
        print()
        print()
        
    x_val = int(input("input x value: "))
    y_val = int(input("input y value: "))

    new_list[y_val][x_val] = ":)"