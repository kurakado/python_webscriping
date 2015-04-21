#!/usr/bin/env python
print "Content-type: text/html\n"
#print html_body % (now.year, now.month, now.day,
#                   now.hour, now.minute, now.second)
print 
import urllib2
import cgi
form = cgi.FieldStorage()
if not form.has_key("site"):
        site="null"
else:
        site   = form["site"].value

#print "site:"+site
if site=="wakame":
        url = "http://jinrou.dip.jp/~jinrou/kako/143356.html"
else:
        url = "http://jinrou.dip.jp/~jinrou/cgi_jinro.cgi?room"
htmldata = urllib2.urlopen(url)
#print unicode(htmldata.read(),"utf-8")
#print "<html><body>"
import html_kaisou
html_kaisou.test_kaisouka(htmldata.read())
#print "</body></html>"
htmldata.close()

