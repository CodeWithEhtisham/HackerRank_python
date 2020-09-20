from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self,data):
        if data.strip():
            print('>>> Data \n{}'.format(data))
    def handle_comment(self,data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            for i in data.split('\n'):
                print(i)
        else:
            print('>>> Single-line Comment \n{}'.format(data))
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()