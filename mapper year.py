#!/usr/bin/env python3

import sys
import datetime

for line in sys.stdin:
    line = line.strip()
    (jour, city, state, cases, dead, ok) = line.split(',')
    datem = datetime.datetime.strptime(jour, "%m/%d/%Y")
    month = datem.month
    year=datem.year
    print('%s\t%s\t%s' % (year,month,cases))
