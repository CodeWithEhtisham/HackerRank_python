m=int(input())
M=set(list(map(int,input().split(" ")[:m])))
n=int(input())
N=set(list(map(int,input().split(" ")[:n])))
# M=set(list(map(int,input().split(" "))[:m]))

# N=set(list(map(int,input().split(" "))[:n]))

# print(M)
# print(N)
S_D=set()
S_D.update(M.symmetric_difference(N))
sort=sorted(S_D)
for i in sort:
    print(i,end="\n")