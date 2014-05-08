__author__ = 'Danny'

import urllib
import urllib2
import cookielib

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
urllib2.install_opener(opener)
req = urllib2.Request("http://www.baidu.com", urllib.urlencode({"username":"root", "password":"ROOTXXOO"}))
req.add_header("Referer", "http://google.com")
resp = urllib2.urlopen(req)
print resp.read()