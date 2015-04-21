#!/usr/bin/env python
from urllib2.request import urlopen
f = urlopen('http://qiita.com/advent-calendar/2014')
f.code
