import urllib2
from HTMLParser import HTMLParser

class rad_parser(HTMLParser):
    

    def handle_data(self,data):
        print data

parser_obj = rad_parser()
url_fetch = raw_input()
print url_fetch
response = urllib2.urlopen(url_fetch)
uri = response.read()

parser_obj.feed(uri)
