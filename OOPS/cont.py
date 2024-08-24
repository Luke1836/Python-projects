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


# List zipping
lst1 = [1,2,3,4]
lst2 = ['a', 'b', 'c']

result = list(zip(lst1, lst2))  # Tuples inside a list
print(result)

# Printing the common elements in the lists
lst3 = [1,2,3,4,5]
lst4 = [2,35,7,4,1]

common = [x for x in lst3 if x in lst4]
print(common)


"""     TUPLES      """
tp1 = (1,3,4,5,"Luke", "Destroyer")
tp2 = ('a','b', 23, 434,34)

concatenated_tp = tp1 + tp2
print(concatenated_tp)  # COntents of tp1 and tp2 are appended together
print(tp1*3) # elements of tp1 is appended thrice

# Methods of tuples
print(tp1.count(1))
print(tp1.index(4)) # finds the index of the element '4' here it is the 2nd position


# Packing and unpacking tuples
packed_tuples = 1, 3.24, 'Hello', 'Profit'
print(packed_tuples)

a,b,c,d = packed_tuples
print(a,b)

a, *b, c = packed_tuples   # Unpacking with '*'; creates a list of the elements from the starting elements to the last element
print(a,b,c)

