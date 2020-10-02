import numpy as np

n,m,p=list(map(int,input().split()))

array1=np.array([list(map(int,input().split())) for _ in range(n)])
array2=np.array([list(map(int,input().split())) for _ in range(m)])

print(np.concatenate([array1,array2],axis=0))

