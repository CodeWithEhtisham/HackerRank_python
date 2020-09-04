N,X=map(int,input().split(" "))
marks=[]
for i in range(X):
    marks.append(map(float,input().split(" ")))
obtain=[]
for i in zip(*marks):
    print(sum(i)/X)