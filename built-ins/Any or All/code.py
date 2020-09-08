n=int(input())
arr=list(map(str,input().split()))
print((all(int(a)>=0 for a in arr) and any(a==a[::-1] for a in arr)))