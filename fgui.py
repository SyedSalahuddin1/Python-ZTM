picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]


for i in picture:
    for z in i:
        if z == 0:
            print(" ", end="")
        elif z == 1:
            print("*", end="")
    print()
    
# Exercise: Check for duplicates in list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = []
for val in some_list:
    if some_list.count(val) > 1:
        if val not in duplicates:
            duplicates.append(val)
print(duplicates)  

            