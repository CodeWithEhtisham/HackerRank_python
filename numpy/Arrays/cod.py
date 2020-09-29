import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr=numpy.array(arr,dtype='float32')[::-1]
    return arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)