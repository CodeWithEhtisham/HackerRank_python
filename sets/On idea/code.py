n,m=map(int,input().split(" "))
array=list(map(int,input().split(" ")[:n]))
A=set(list(map(int,input().split(" ")[:m])))
B=set(list(map(int,input().split(" ")[:m])))
# happiness=0
print(sum((i in A)-(i in B) for i in array))
# for i in array:
#     if i in A:
#         happiness+=1
#     else:
#         happiness-=1
# print(happiness)