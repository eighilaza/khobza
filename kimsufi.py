import httplib
c = httplib.HTTPConnection('www.google.com')
c.request("HEAD", '')
if c.getresponse().status == 200:
   print('web site exists')
else: 
   print('cannot reach web site')
