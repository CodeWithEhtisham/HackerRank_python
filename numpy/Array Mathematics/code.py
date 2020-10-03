import numpy as np

m,n=list(map(int,input().split()))

A=np.array([list(map(int,input().split())) for _ in range(m)])
B=np.array([list(map(int,input().split())) for _ in range(m)])

print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(A//B)

print(np.mod(A,B))
print(np.power(A,B))
