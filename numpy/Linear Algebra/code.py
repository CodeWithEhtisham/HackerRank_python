import numpy as np
n=int(input())
a=[list(map(float,input().split())) for _ in range(n)]
deter=np.linalg.det(a)
print(round(deter,2))
