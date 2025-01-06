# Evite mais de duas expressões em abrangências de lista

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print(squared) 

my_lists = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
]

flat2 = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]

print(flat2)

flat3 = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat3.extend(sublist2)

print(flat3)