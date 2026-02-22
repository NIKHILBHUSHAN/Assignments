'''import numpy as np

scores=np.array([[[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]],[[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]])
print(scores)
print(type(scores))
print(np.__version__)
print(scores.ndim)

arr=np.array([1, 2, 3, 4, 5],ndmin=5)
print(arr)
print(arr.ndim)

array=np.array([1,2,3,4])
copy=array.copy()
array[0]=0
print(array)
print(copy)

array1=np.array([11,22,33,44])
x=array1.view()
x[0]=0
print(array1)
print(x)

print(copy.base)
print(x.base)'''

'''import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)'''

import numpy as np
arr1 = np.array([1, 2, 3, 4], ndmin=5)

print(arr1)
print('shape of array :', arr1.shape)