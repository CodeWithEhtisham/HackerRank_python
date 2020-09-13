# import re

# s = input()
# k = input()
# index = 0

# if re.search(k, s):
#     while index+len(k) < len(s):
#         m = re.search(k, s[index:]) #begins search with new index
        
#         print("({0}, {1})".format(index+m.start(), index+m.end()-1)) 
        
#         index += m.start() + 1 #assign new index by +1 
# else:
#     print((-1, -1))

import re
s, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')