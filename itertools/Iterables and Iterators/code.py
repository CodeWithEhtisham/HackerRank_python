# import itertools

# first=int(input())

# string=list(map(str,input().split(" ")))

# k=int(input())

# ls=[]
# count=0
# for i in itertools.combinations(string,k):
#     ls.append(i)
#     for j in range(k):
#         if string.index(string[j]) in i:
#             count+=1
# print(count)

from itertools import combinations

_,s,n = input(),input().split(),int(input())
t = list(combinations(s,n))
f = [i for i in t if 'a' in i]
print("{0:.3}".format(len(f)/len(t)))