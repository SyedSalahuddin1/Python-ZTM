picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for nums in picture:
    for ones in nums:
        if ones == 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()

# Exercise: Check for duplicates in list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = []
 
for alphabets in some_list:
    if some_list.count(alphabets) > 1:
        if alphabets not in duplicates:
            duplicates.append(alphabets)
print(duplicates)

            