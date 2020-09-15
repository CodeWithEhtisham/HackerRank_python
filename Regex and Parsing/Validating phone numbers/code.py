# import re
# n=int(input())
# regex=r'(7|8|9)[1-9]{10}'
# for i in range(n):
#     print(re.search(regex,input()))
import re
[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]