import collections
dicts=collections.defaultdict(list)
n=int(input())
for i in range(n):
    dicts[input()].append(int(i))

print(len(dicts.keys()))
for i,j in dicts.items():
    print(len(j),end=" ")