from html.parser import HTMLParser

class parser(HTMLParser):
    def handle_starttag(self,tag,arrts):
        print(tag)
        for tags,value in arrts:
            print('-> {} > {}'.format(tags,value))
    # def handle_data(self,data):
html=''
for i in range(int(input())):
    html+=input()
# print(html)
myparser=parser()
myparser.feed(html)
