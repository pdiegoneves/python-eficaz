# Use abrangências de lista (list comprehensions) em vez de map e filter

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

squares2 = map(lambda x: x**2, a)
print(list(squares2))


even_squares2 = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(even_squares2))
