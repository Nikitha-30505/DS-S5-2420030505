# numpy - numerical python
# np - alias name of numpy
# pip install numpy
# ndim - number of dimensions

import numpy as np

# Example 1 - (1D)
print("Example 1")
N = np.array([10,65,34,90])
print(N)
print()   # Blank line

# Example 2 - by passing lists (2D)
print("Example 2")
P = np.array([[1,2,3],[4,5,6]])
print(P)
print()

# Example 3 - using ndarray.ndim (0D)
print("Example 3")
S = np.array(23)
print(S.ndim)
print()

# Example 4 - using [] brackets (1D)
print("Example 4 ")
S = np.array([23])
print(S.ndim)

# Example 5 - zero matrix

print("Example 5")

P = np.zeros([1])
print(P)
print(type(P))

N = np.zeros([3,4])
print(N)
print(type(N))
print()

# Example 5 - ones matrix

print("Example 6")

P = np.ones([1])
print(P)
print(type(P))

N = np.ones([3,4])
print(N)
print(type(N))
print()

#Array slicing

P=np.array([1,2,3,4,5])
print(n[-1])
P=np.array([[1,2,3],[6,7,8]])
print(n[0,-1])
print(p[2:5]) #int includes element at index 2 and excludes element at index 5
print(p[:5])  #from frist element upto 4th index
print(p[4:])  #starting from 4th index to last index

# step 
# Array([start:end:step])