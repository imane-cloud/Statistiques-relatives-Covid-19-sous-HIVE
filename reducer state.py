#!/usr/bin/env python3

from operator import itemgetter
import sys
current_state = None
current_sum=0
state = None
for line in sys.stdin:
    line = line.strip()
    state, cases = line.split('\t', 1)
    try:
        cases= int(cases)
    except ValueError:
        continue
    if current_state == state:
        current_sum+=cases
    else:
        if current_state:
            print ('%s\t%s' % (current_state, current_sum))
        current_state = state
        current_sum= cases
if current_state== state:
    print ('%s\t%s' % (current_state, current_sum))

