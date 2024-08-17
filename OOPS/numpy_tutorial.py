import numpy as np
import random as r

a = np.array([1,2,3,4,5], dtype="int32")
b = np.array([[1.0, 2.0, 3.0, 8.0, 9.0], [4.0, 5.0, 6.0, 7.0, 10.0]])
#c = b.copy()
c = np.full((5,2), 4)
d = np.matmul(b,c)  # Matrix Multiplication
print(np.linalg.det(d))

""" https://docs.scipy.org/doc/numpy/reference/routines.linalg.html
https://docs.scipy.org/doc/numpy/reference/routines.math.html """

""" 
print(b.ndim)
print(b.shape, a.itemsize)
print(b[: , 2])  All the rows in the third column
print(b[0, :])  All the columns in the first row 
print(b[0, 0::2]) For the first row , start from the first column, move two positions to the right, select that element. """

""" c = np.zeros((2,5), dtype="int32")
print(c)

# Create an array with all eleements equal to 99
d = np.full((4,4), 88)
print(d)

print(np.random.rand(3,4))
print(np.identity(4))
print(np.random.randint(-2, 2, size=(4,4))) """


""" z = np.identity(4)
print(z)

y = np.ones([4,4])
x = np.zeros([2,2])

y[1:-1,1:-1] = x # [1:3, 1:3]
print(y) """

data = np.genfromtxt('data.txt', delimiter=',')
data = data.astype('int32')
print(data)