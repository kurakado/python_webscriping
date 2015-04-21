#!/usr/bin/env python

def bs4():
    import urllib2
    import cgi
    from bs4 import BeautifulSoup
    form = cgi.FieldStorage()
    if not form.has_key("site"):
            site="null"
    else:
            site   = form["site"].value
    import sys 
    if len(sys.argv)!=1:
            url = sys.argv[1]
    elif site=="wakame":
            url = "http://jinrou.dip.jp/~jinrou/kako/143356.html"
    else:
            url = "http://jinrou.dip.jp/~jinrou/cgi_jinro.cgi?room"
    filename=url.split("/")
    filename=filename[len(filename)-1]
    import subprocess
    cmd="wget %s" % url
    cmd=cmd.split()
    ret = subprocess.call(cmd)
    if ret!=0:
            return ret
    html_doc=open(filename,"r").read()

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc)

    print(soup.prettify())



if __name__=="__main__":
    bs4()
