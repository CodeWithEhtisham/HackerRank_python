n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(0,N):
    ls=input().split(" ")
    if len(ls)==1:
        s.pop()
    else:
        if ls[0]=="discard":
            s.discard(int(ls[1]))
        else:
            s.remove(int(ls[1]))
print(sum(s))