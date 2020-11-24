#!/usr/bin/env python
import sys

class AccidentTotalReducer:
    make_year = None
    accidentTotal = 0

    def reduce(self):
        for line in sys.stdin:
            key, count = line.split("\t")

            try:
                count = int(count)
            except ValueError:
                continue

            if self.make_year == key:
                self.accidentTotal += count
            else:
                if self.make_year:
                    print('{}\t{}'.format(self.make_year, self.accidentTotal))

                self.accidentTotal = count
                self.make_year = key

        if self.make_year == key:
            print('{}\t{}'.format(self.make_year, self.accidentTotal))


# do not forget to output the last group if needed!
if __name__ == "__main__":
    accidentTotal = AccidentTotalReducer()
    accidentTotal.reduce()
