# scipy matlab arrays: Exporting the data in Matlab format
# for converting or export we use savemat(). 
# here we have 3 parameters: 1.filename, 2.mdict, 3.do_compression

# example: here now we will export  the below arrays as variable name "vec" to mat file.
from scipy import io
import numpy as np 
array1 = np.arange(10)
io.savemat('arrays1.mat', {"vec": array1}) 


# here now we will import  the existing  mat file.
# it  have only 1 parameter that is filename:
from scipy import io
import numpy as np 
array2 = np.array([0,1,2,3,4,5,6,7,8,9])
# Export
io.savemat('array2.mat', {"vec": array1}) 
# Import
array2new = io.loadmat('array2.mat',squeeze_me =True)
print(array2new['vec'])






