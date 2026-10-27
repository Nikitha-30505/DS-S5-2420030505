#ex 10 - 

import numpy as np
from scipy.spatial import distance

pointA=np.array([2,4,6])
pointB=np.array([5,1,9])
manhattan_dist=distance.cityblock(pointA,pointB)
print("Manhattan Distance:", manhattan_dist)

#Similarity(inverse of distance)
similarity_manhattan=1/(1+manhattan_dist)
print("Mahattan Similarity:", similarity_manhattan)


#ex 11 - minkowski

minkowski_dist_p3=distance.minkowski(pointA,pointB,p=2)
print("Minkowski Distance(p=3):", minkowski_dist_p3)

#inverse of distance
similarity_minkowski=1/(1+minkowski_dist_p3)
print("Minkowski similarity(p=2):", similarity_minkowski)

# p= 1
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=1)
print("Minkowski Distance(p=1):", minkowski_dist_p3)

#inverse
similarity_minkowski=1/(1+minkowski_dist_p3)
print("Minkowski similarity(p=1):", similarity_minkowski)

#p=3
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=3)
print("Minkowski Distance(p=3):", minkowski_dist_p3)