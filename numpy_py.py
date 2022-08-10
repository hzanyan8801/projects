
import numpy as np 

"""
# 0-D Arrays
arr = np.array(42)

print(arr)

# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])

print(arr)

# 2-D Arrays
arr = np.array([[1, 2, 3], [ 4, 5, 6]])

print(arr)



# 3-D Arrays
arr = np.array([[[1, 2, 3], [ 4, 5, 6]],[[1, 2, 3], [ 4, 5, 6]]])

print(arr)

"""

arr = np.array([1, 2, 3, 4], ndmin = 5)

print(arr)
print('number of dimensions :', arr.ndim)
