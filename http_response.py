import urllib2
http_response=urllib2.urlopen('http://www.yahoo.com')
print http_response.code
