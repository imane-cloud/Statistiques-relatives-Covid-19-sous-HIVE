#!/usr/bin/env python3

from operator import itemgetter
import sys
import datetime
current_month = None
current_cases = None
counter=0
month = None
for line in sys.stdin:
    line = line.strip()
    month, cases = line.split('\t', 1)
    try:
        cases = int(cases)

    except ValueError:
        continue
    if current_month == month:
        current_cases+= cases
        counter+=1
    else:
        if current_month:
            print('%s\t%i'% (current_month, current_cases/counter))
        current_month = month
        current_cases = cases
if current_month == month:
    print ('%s\t%f' % (current_month, current_cases/(1+counter)))
