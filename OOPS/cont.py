## List comprehension

square = [num **2 for num in range(11)]
print(square)

indices = [[i,j] for i in square for j in square]
print(indices)

lst = [1,11,2,3,3,12,2,31,3,12,13,3,2]
print(lst)

# Removing repeating numbers
lst = list(set(lst))
print(lst)

# Matrix operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]
]

print(len(matrix)) # Number of rows
print(len(matrix[0])) # Number of columns

tranposed_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(tranposed_matrix)