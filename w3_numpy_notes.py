import numpy as np #import as alias, most people use np
import pandas as pd
#import matplotlib.pyplot as plt #very good graphing library...

##Array Dimensions
#Scalar or 0d array
arr = np.array(42)
print(arr)
#1d array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#2d arrays are arrays with multiple 1d arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr) #each new array gets printed on next line
#a 3d array has multiple 2d arrays in it
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)#extra line break between 3d arrays when printed
#Check the number of dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#set number of dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr) #prints: [[[[[1 2 3 4]]]]]
print('number of dimensions :', arr.ndim)


##Accessing Arrays
#access the same as normal
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1]) #2
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) #6
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) #negative indexing, prints 10
#splicing arrays syntax: [start:end:step] -if no start = 0, if no end = the end of arr, if no step = 1
#start inclusive, end exclusive
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #2-5 //6 excluded
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:]) #5-7
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4]) #1-4 //5 excluded
#negative slicing ---the end is not 0 as one would expect, but -1.....
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) #prints 5,6
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) #step 2, prints 2 4
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2]) #prints every other elem starting at 0
#slicing 2d arr
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #7,8,9
#from multiple arrays slice a number or range...
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
#or could slice this way:
print(arr[:,2]) #prints 3, 8
#slice a range from a range of arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) #prints [[2 3 4] [7 8 9]]


##Data Types
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
#check data type
arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int64
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) #U6 //unicode
#explicitly set the data type of an arr
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype) #S1
#For i, u, f, S and U we can define size as well.
#Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr) #[1 2 3 4]
print(arr.dtype) #int32
#Change data type
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr) #[1 2 3]
print(newarr.dtype) #int32
#change to bool arr
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr) #[True False True]
print(newarr.dtype)


##Copy Array
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr) #[42, 2, 3, 4, 5]
print(x) #[1, 2, 3, 4, 5] !<-- x is now a copy of arr, and will not be modified when arr changes
##^^Same example without copy:
arr = np.array([1, 2, 3, 4, 5])
x = arr
arr[0] = 42
print(arr) #[42, 2, 3, 4, 5]
print(x) #[42, 2, 3, 4, 5] !<--- x was changed also when updating arr

##View
#when using view, both the original, and the view array are both changed if one or the other is updated
#seems to work the same as x = arr ?????
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr) #[42, 2, 3, 4, 5]
print(x) #[42, 2, 3, 4, 5]

##Array Ownership
#copies owns the data, and views does not own the data
#the attribute base that returns None if the array owns the data.
#Otherwise, the base  attribute refers to the original object.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base) #None
print(y.base) #[1 2 3 4 5]


##Array Shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) #prints (2 4) -two dimensions, 4 items each arr

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

#reshape an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) #1st dim 4 items, 2nd dim 3 items
print(newarr) #prints [[1 2 3] [4 5 6] [7 8 9 ] [10 11 12]]

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2) #1st dim 2 items, 2nd dim 3 items, 3rd dim 2 items
print(newarr) 
'''
	[
	  [
	    [1 2]
	    [3 4]
	    [5 6]
	  ]   
	  [
	    [7 8]
	    [9 10] 
	    [11 12]   
	  ]
	]  
'''

##reshaping is just a view, it doesn't modify the original array

#can have an unknown dim
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#flatten an array (convert to 1d)
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

#other reshaping methods (not covered):
# flatten, ravel, rot90, flip, fliplr, flipud etc. 


##Iteration
#1d
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
'''
1
2
3
'''

#2d
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
'''
[1 2 3]
[4 5 6]
'''  

#get scalars, have to iterate each dim
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)
'''
1
2
3...
'''

#In basic for loops, iterating through each scalar of an array we need to use n for loops...
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  #print('x ',x)
  for y in x:
    #print('y ', y)
    for z in y:
      print(z) #iterates all the scalars (individual values)


#nditer (iterate n# of dimensions = nditer)
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

#iterate with the index
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
'''
(0,) 1
(1,) 2
(2,) 3
'''



#iterate with the index multidim arr
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
'''
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
'''


#Numpy Math
a = np.array([1,2,3,4])
print(a + 2) # [3 4 5 6]
print('A',a) #A [1 2 3 4] ##doesn't change...remember needs assignent to change
a = a + 2
print(a)
