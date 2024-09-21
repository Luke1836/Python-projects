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
lst.pop() # Removes the last element from the list
print(lst)

print(lst.copy())

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


"""     SETS       """
set1 = {1,2,3,4,53,2}
set2 = {2,4,2,4,42,53}

union_set = set1.union(set2)
intersection_set= set1.intersection(set2)
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

print(set1, set2, union_set, intersection_set, difference_set1, difference_set2)
set1.intersection_update(set2)
set2.difference_update(set1)
print(set1, set2)


"""     Dictionaries      """       # Dictionary comprehension
dict1 = {x:x**2 for x in range(6)}
print(dict1)
dict2 = {x:x**3 for x in range(6) if x%2 == 0}
print(dict2)

# Count the frequency of elements in the list
lst = [1,2,4,2,3,21,42,3,23,13,13,2,4,23,2,2,32]
dict = {x:lst.count(x) for x in lst}
print(dict)

# Merging two dictionaries
dict3 = {**dict1, **dict2}
print(dict3)

for key, values in dict3.items():
    print(f'Key: {key},\tValue: {values}')