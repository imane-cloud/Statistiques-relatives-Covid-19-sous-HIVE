#!/usr/bin/env python3

from operator import itemgetter
import sys
import datetime
current_year= None
current_cases= 0
current_sum=0
year = None
for line in sys.stdin:
    line = line.strip()
    year, cases = line.split('\t', 1)
    try:
        cases= int(cases)
    except ValueError:
        continue
    if current_year == year:
        current_sum+=cases
    else:
        if current_year:
            print ('%s\t%s' % (current_year, current_sum))
        current_year = year
        current_sum= cases
if current_year== year:
    print ('%s\t%s' % (current_year, current_sum))
