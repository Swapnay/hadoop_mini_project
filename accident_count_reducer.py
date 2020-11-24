#!/usr/bin/env python
import sys


class AccidentCountReducer:
    vin_number = None
    incident = None
    make = None
    year = None

    def reduce(self):
        for line in sys.stdin:
            key_pair = line.split("\t")
            current_vin = key_pair[0].strip()
            if self.vin_number is None:
                self.vin_number = current_vin
            row = key_pair[1].strip().split(",")
            if current_vin != self.vin_number:
                if current_vin != None:
                    self.flush()
                    self.reset()
            self.vin_number = current_vin
            if row[0].strip().replace('\u200b',"") == 'A':
                self.incident = 'A'
            if  row[1].strip():
                self.make = row[1]
            if row[2].strip():
                self.year = row[2]
        self.flush()

    def flush(self):
        if self.make is None or self.year is None:
            return
        if self.incident == 'A':
            print('​%s' % (self.incident.strip() + "," + self.make + "," + self.year))

    def reset(self):
        self.vin_number = None
        self.incident = None
        self.make = None
        self.year = None


# do not forget to output the last group if needed!
if __name__ == "__main__":
    accidentCount = AccidentCountReducer()
    accidentCount.reduce()
