# working with spatial data: it refers to data that is represented in a geometric space
# Triangulation: one method to generate this traingulation through the point is delaunay()
# here now we will create a traingulation from some points:

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

array1 = np.array([[2,4],[3,4],[3,0],[2,2],[4,1]])
array1new = Delaunay(array1).simplices
plt.triplot(array1[:,0], array1[:,1],array1new)
plt.scatter(array1[:,0], array1[:,1],color='r')
plt.show()


# Convex Hull : it is basically the smallest polygon that cover all of the given point:
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

array2 = np.array([[2,4], [3,4], [3,0], [2,2], [4,1], [1,2], [5,0], [3,1], [1,2], [0,2]])

hull = ConvexHull(array2)
hull_points = hull.simplices
plt.scatter(array2[:,0],array2[:,1])
for i in hull_points:
    plt.plot(array2[i,0],array2[i,1],'k-')
plt.show()



# KDTress : they are a data structure optimized for the nearest neighbour quaries
from scipy.spatial import KDTree
array3 = [(1,-1), (2,3), (-2,3), (2,-3)]
tree = KDTree(array3)
res = tree.query((1,1))
print(res)


# Distance matrix: it is used to find the various types of distance between two points
# There are basically two types : 1.Euclidean Distance, 2.Cosine Distance

# 1.Euclidean Distance:
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10,2)
distance = euclidean(p1,p2)
print(distance)

# 2.Cosine Distance

from scipy.spatial.distance import cosine
p1 = (1,0)
p2 = (10,2)
distance = cosine(p1,p2)
print(distance)



