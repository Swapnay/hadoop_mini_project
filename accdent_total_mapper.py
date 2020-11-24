#!/usr/bin/env python
import sys
#row = [(self.incident + "," + self.make + "," + self.year)]
total=0
for line in sys.stdin:
    row = line.split(",")
    key = row[1] + row[2]
    print('%s\t%s' % (key.strip(),1))