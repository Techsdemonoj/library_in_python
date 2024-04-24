# working with graph: we have a module nmaed scipy.sparse.csgraph
# adjacency Matrics: nxn matrix, where n is the number of elements in the graph.
# connected component:
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
array3 = np.array([[0,1,2],[1,0,0],[2,0,0]])
array3new = csr_matrix(array3)
print(connected_components(array3new))

# dijkstra method: for finding the shortest path in a graph from
# in a graph from one elements to another .
# its takes 3 arguments: return_predecessors, indices, limit 
# here we will find the shortest path from elements 1 to 2:
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
array3 = np.array([[0,1,2],[1,0,0],[2,0,0]])
array3new = csr_matrix(array3)
print(dijkstra(array3new,return_predecessors=True, indices=0))


# Floyd warshall() method 

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
array3 = np.array([[0,1,2],[1,0,0],[2,0,0]])
array3new = csr_matrix(array3)
print(floyd_warshall(array3new, return_predecessors=True))



# Bellman_ford() method: for finding the shortest path in a graph from
# between all the pairs of elements but this method can handle negetive
# weight as well.
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix
array3 = np.array([[0,1,2],[1,0,0],[2,0,0]])
array3new = csr_matrix(array3)
print(bellman_ford(array3new,return_predecessors=True,indices=0))


# Depth first order: it returns a depth first traversal from node: it has 2 arguments
# 1.the graph, 2. starting element.
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix
array4 = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
array4new = csr_matrix(array3)
print(depth_first_order(array4new,1))


# breadth_first_order() method: its returns the breadth from a node
# it has 2 arguments  :  1.the graph, 2. starting element.
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
array4 = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
array4new = csr_matrix(array3)
print(breadth_first_order(array4new,1))













