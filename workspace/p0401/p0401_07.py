# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 2, 4, 16, 6]
# num_dict = {}

# for i in num_list:
#     # 딕셔너리에 추가
#     if (i not in num_dict):
#         num_dict[i] = 0
#     num_dict[i] = num_dict[i] + 1 # 키가 몇 개 존재하는가
# print(num_dict)

# for i, d in enumerate(num_dict):
#     print("{} : {}".format(i, num_dict[d]))
    
artist_list = [
    "the Weeknd", "Linkin Park", "Calvin Harris", "Future", "SZA",
    "the Weeknd", "Linkin Park", "Calvin Harris", "Future", "SZA",
    "the Weeknd", "Linkin Park", "Calvin Harris", "Future", "SZA",
    "Kanye West", "Arctic Monkeys", "Avicii"
    ]

artists = {}

for artist in artist_list:
    if (artist not in artists):
        artists[artist] = 1
    else:
        artists[artist] = artists[artist] + 1
print (artists)

art_list = []
art_num = []
for key, value in artists.items():
    print("{} : {}".format(key, value))
    art_list.append(key)
    art_num.append(value)
print(art_list)
print(art_num)
 
tuple_art = tuple(art_list)
print(tuple_art)
print()
print(list(zip(art_list, art_num))) 
print(dict(zip(art_list, art_num))) 

