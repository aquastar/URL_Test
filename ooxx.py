__author__ = 'Danny'

#import cookie_lib
import urllib2
import re

HOST_ADD = 'http://localhost/SocialServer'
right_count = 0
wrong_count = 0

## [optinal] cookie could be set by following codes.
#cj = cookie_lib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#opener.addheaders = [ ('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
#urllib2.install_opener(opener)

## data should be in such a format
# URL|post_data|expected returned result
# e.g. /index.php?app=api|username=root&password=xxoo|{"status":0,"data":"no auth"}

for line in open('data'):
    if re.search(r'^#', line):
        continue
    line_arr = line.split('|')

    ## initial request
    req_url = HOST_ADD + line_arr[0]
    req_data = line_arr[1]

    req = urllib2.Request(req_url, req_data)

    ## [optinal] refer could be set by following codes.
    # req.add_header("Referer", "http://google.com")

    ## send request and process it
    res = urllib2.urlopen(req).read()
    rst = (line_arr[2].strip() == res)

    if rst is True:
        right_count += 1
    elif rst is False:
        wrong_count += 1

    print "request [ " + req_url + " ] with [ " + req_data + " ]"
    print "response is [ " + str(res) + " ]"
    print "expected is [ " + line_arr[2].strip() + " ]"
    print "result is [ " + str(rst) + " ]"
    print "==============="

print "\n[Summary]"
print "use case count   is [ " + str(right_count + wrong_count) + " ]"
print "right case count is [ " + str(right_count) + " ]"
print "wrong case count is [ " + str(wrong_count) + " ]"

