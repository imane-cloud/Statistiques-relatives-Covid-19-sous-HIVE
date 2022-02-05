#!/usr/bin/env python3

import sys
import datetime

for line in sys.stdin:
    line = line.strip()
    (jour, city, state, cases, dead, ok) = line.split(',')
    datem = datetime.datetime.strptime(jour, "%m/%d/%Y")
    year=datem.year
    month=datem.month
    print('%s\t%s\t%s' % (month,year,cases))
