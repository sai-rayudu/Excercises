import numpy as np
print(np.__version__)   #returns version
arr=np.array([1,2,3])   # new array creation
print(arr)
arr1=np.array([[1,2,3],[4,7,8]]) # multi-dimentional array
print(arr1.shape)  #return no.of rows and cols in tuple
print(arr1.size)  # returns no of elements inside array
arr3d = np.array([
    [[1, 2, 3], [4, 5, 6]],    # Layer 1 (2 rows, 3 columns)
    [[7, 8, 9], [10, 11, 12]]  # Layer 2 (2 rows, 3 columns)
])
print(arr3d.ndim) #returnns how many dimentions the array has
print(arr3d.itemsize)  # returns how many bytes each item takes
print(arr3d.nbytes)  # returns total bytes the array has taken in bytes
print(arr3d[1][1][0])  # access throw index
print(arr3d[1,1,0])  # access throw index
print(arr[0:2])  # slicing
l=[23,45,67]  #list
arr4=np.asarray(l)
print(type(arr4))
arr5=np.arange(0,100,1)  #create array withe range method
print(arr5)
arr6=np.linspace(0,1,5)  # create an array with 5 numbers betten 0,1
print(arr6)
arr7=np.zeros((2,3)) #it returns 2*3 array filled with zeros
print(arr7)
arr8=np.ones((2,3)) #it creates 2*3 array filled with ones
print(arr8)
arr9=np.empty((2,3)) #it creates an 2*3 array filled with random values
print(arr9)
arr10=np.empty((1,3)) #it creates an 2*3 array filled with random values
print(arr10)
arr11=np.arr.astype(float)  # changes the type
print(arr11.dtype)
arr12=arr11.copy()  # returns its copy
print(arr12)
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.sum())
print(arr.prod())
print(arr.std())
print(arr.var())
rand_arr = np.random.rand(3)
print(rand_arr)
rand_int = np.random.randint(1, 10, size=3)
print(rand_int)