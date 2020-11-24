#!/usr/bin/env python
import sys
#input_csv.columns = ['incident_id', 'incident_type', 'vin_number', 'make','model','year','Incident_date','description']
for line in sys.stdin:
    row = line.split(",")
    vin_number = row[2]
    incident_type = row[1]
    make = row[3]
    year =row[5]
    print('%s​\t​%s' % (vin_number.strip(), incident_type.strip()+','+make +','+year ))