from collections import deque
d=deque()

n=int(input())

for i in range(n):
    ls=list(input().split(" "))
    if len(ls)==1:
        action=ls[0]
    else:
        action=ls[0]
        value=ls[1]
    if action=="append":
        d.append(int(value))
    elif action=="appendleft":
        d.appendleft(int(value))
    elif action=='pop':
        d.pop()
    else:
        d.popleft()

[print(i,end=" ") for i in d]