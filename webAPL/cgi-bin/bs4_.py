#!/usr/bin/env python
print "Content-type: text/html\n"

from bs4 import BeautifulSoup
import bs4_html
soup=bs4_html.bs4()

print soup.prettify()
