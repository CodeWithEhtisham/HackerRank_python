import numpy
M =int(input())
array1 =numpy.array([input().split() for _ in range(M)],int)
array2 =numpy.array([input().split() for _ in range(M)],int)
numpy.set_printoptions(sign=" ")
print(numpy.dot(array1, array2)) 