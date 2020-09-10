# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regex = r'^[-+]?[0-9]*\.[0-9]+$'


n=int(input())
for i in range(n):

    print(bool(re.search(regex,input())) )