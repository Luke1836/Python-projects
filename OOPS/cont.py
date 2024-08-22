## List comprehension

square = [num **2 for num in range(11)]
print(square)

indices = [[i,j] for i in square for j in square]
print(indices)sdf