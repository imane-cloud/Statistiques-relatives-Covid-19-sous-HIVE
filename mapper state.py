import sys
import datetime

for line in sys.stdin:
    line = line.strip()
    (jour, city, state, cases, dead, ok) = line.split(',')
    print('%s\t%s' % (state,cases))
