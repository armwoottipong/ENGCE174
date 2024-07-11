squares = [x**2 for x in range(10)]
print (squares)


square = {x: x**2 for x in range (5)}
print(square)


even_squares = { x**2 for x in range(10) if x % 2 == 0 }
print(even_squares)