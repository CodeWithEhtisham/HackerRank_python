import numpy as np
m,n=list(map(int,input().split()))
b=np.array([list(map(int,input().split())) for _ in range(m)])
np.set_printoptions(legacy='1.13')
print(np.mean(b, axis = 1))
print(np.var(b, axis = 0))
print(np.std(b))