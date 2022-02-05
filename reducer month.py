#!/usr/bin/env python3

from operator import itemgetter
import sys
import datetime
current_month = None
current_sum = 0
month = None
for line in sys.stdin:
    line = line.strip()
    month, cases = line.split('\t', 1)
    try:
        cases = int(cases)
    except ValueError:
        continue
    if current_month == month:
        current_sum += cases
    else:
        if current_month:
            print('%s\t%s' % (current_month,current_sum))
        current_month = month
        current_sum = cases
if current_month == month:
    print ('%s\t%s' % (current_month, current_sum))


