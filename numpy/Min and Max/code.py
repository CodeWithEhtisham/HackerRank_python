import numpy as np
m,n=list(map(int,input().split()))
array=np.array([list(map(int,input().split())) for _ in range(m)])
print(np.max(np.min(array,axis=1)))
