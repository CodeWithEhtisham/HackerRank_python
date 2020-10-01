import numpy

n,m=input().split()

array=numpy.array([list(map(int,input().split())) for _ in range(int(n))])
print(array.transpose())
print(array.flatten())