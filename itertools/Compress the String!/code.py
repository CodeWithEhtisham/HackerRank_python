import itertools

s=input()

ls=[(len(list(cs)),str("'{}'".format(c))) for c,cs in itertools.groupby(s)]
for i in ls:
    print(i,end=" ")