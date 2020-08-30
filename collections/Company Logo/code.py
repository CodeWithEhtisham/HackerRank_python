# import math
# import os
# import random
# import re
# import sys
# from collections import defaultdict


# if __name__ == '__main__':
#     s = input()
#     d=defaultdict(list)
#     for i in s:
#         d[i].append(len(re.findall(i,s)))
#     # print(d)
#     dic=sorted(d, key=lambda k: len(d[k]), reverse=True)
#     for i in dic[:3]:
#         print(i,len(d[i]))
    

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]