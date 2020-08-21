a=int(input())
A=set(map(int,input().split(" ")))
n=int(input())
for i in range(n):
    operation,number=input().split()
    if operation=="intersection_update":
        ls=set(map(int,input().split()))
        A.intersection_update(ls)
    elif operation=="update":
        ls=set(map(int,input().split()))
        A.update(ls)

    elif operation=="symmetric_difference_update":
        ls=set(map(int,input().split()))
        A.symmetric_difference_update(ls)

    elif operation=="difference_update":
        ls=set(map(int,input().split()))
        A.difference_update(ls)
    else:
        pass
        
print(sum(A))