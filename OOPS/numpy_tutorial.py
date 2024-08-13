import numpy as np

a = np.array([1,2,3,4,5], dtype="int32")
b = np.array([[1.0, 2.0, 3.0, 8.0, 9.0], [4.0, 5.0, 6.0, 7.0, 10.0]])

""" print(b.ndim)
print(b.shape, a.itemsize)
print(b[: , 2])  All the rows in the third column
print(b[0, :])  All the columns in the first row 
print(b[0, 0::2]) For the first row , start from the first column, move two positions to the right, select that element. """