# def highest_even(li):
#     greatest = li[0]
#     for i in li:
#         if i % 2 == 0:
#             if i > greatest:
#                 greatest = i
#     return greatest

# print(highest_even([10, 22, 3, 4, 25]))

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even([100, 22, 3, 4, 25]))
