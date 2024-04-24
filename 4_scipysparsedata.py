# What is sparse data: Sparse data is the data that has mostly unused elements,
# like the elements that dont carry any information, [1,0,2,23,4,5,6,7,8,9]
# sparse data example : [1,0,2,0,3,0,0,0,0,4]
# dense array: [2,5,6,8,9,7,1,2,3,6]

# how to sparse data.
# scipy has module scipy.sparse fuction. 
# there are 2 matrics in  this sparse. 1. CSC(compressed spare column), 2.CSR(compressed sparse row)

# CSR matrics: here we will create  a CSR matrics from an array
import numpy as np
from scipy.sparse import csr_matrix
array1 = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(array1))

# sparse matrix Methods
import numpy as np
from scipy.sparse import csr_matrix
array2 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(array2).data)


# what if we want to count nonzeros, we can do this via count_nonzero() method
import numpy as np
from scipy.sparse import csr_matrix
array2 = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(array2).count_nonzero())


# for removing the zero elements from the matrix we will use elements_zero() method
import numpy as np
from scipy.sparse import csr_matrix
array2 = np.array([[0,0,0],[0,0,1],[1,0,2]])
array2new = csr_matrix(array2)
array2new.eliminate_zeros()
print(array2new)


# elemeinating duplicate entrys with the sum_duplicate() method
import numpy as np
from scipy.sparse import csr_matrix
array2 = np.array([[0,0,0],[0,0,1],[1,0,2]])
array2new = csr_matrix(array2)
array2new.sum_duplicates()
print(array2new)


# Here we will convert csr to csc with the tocsc() method
import numpy as np
from scipy.sparse import csr_matrix
array2 = np.array([[0,0,0],[0,0,1],[1,0,2]])
array2new =csr_matrix(array2).tocsc()
print(array2new)





