# Enter your code here. Read input from STDIN. Print output to STDOUT
# from HTMLParser import HTMLParser
from html.parser import HTMLParser
class myparser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('Start : {}'.format(tag))
        # print("-> {} > {}".format(arrt,arrt.value))1
        for key,value in attrs:
            print("-> {} > {}".format(key,value))
    def handle_endtag(self,tag):
        print('End   : {}'.format(tag))
    
    def handle_startendtag(self, tag, attrs):
        # return super(myparser, self).handle_startendtag(tag, attrs)
        print('Empty : {}'.format(tag))
        for key,value in attrs:
            print("-> {} > {}".format(key,value))



if __name__ == "__main__":
    parser=myparser()
    for i in range(int(input())):
        parser.feed(input())
