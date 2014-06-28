#simple url fetching using Python
import urllib2

#response data

response = urllib2.urlopen("http://radhasundar.weebly.com")

#response output

data = response.read()

print data
