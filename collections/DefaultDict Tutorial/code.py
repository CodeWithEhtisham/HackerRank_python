# Enter your code here. Read input from STDIN. Print output to STDOUT
# n,m=map(int,input().split(" "))

# from collections import defaultdict
# df=defaultdict(list)

# for i in range(n):
#     df["A"].append(input())
# for i in range(m):
#     df["B"].append(input())

# for i,j in enumerate(df["B"]):
#     for k in range(len(df["A"])):
#         if df["A"][k]==j:
#             print(k+1,end=" ")
#     if j not in df["A"]:
#         print(-1)

#     print("")
from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1,n+1):
    d[input()].append(str(i))
    
for i in range(m):
    print (' '.join(d[input()]) or -1)