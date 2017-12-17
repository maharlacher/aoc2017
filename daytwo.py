# daytwo_checksum

import csv

checksum = 0

with open("daytwo_input.tsv") as tsv:
  for line in csv.reader(tsv, dialect="excel-tab"):
      max = 0
      min = 10000
      for idx in range(len(line)):
          if int(line[idx]) > max:
              max = int(line[idx])
              print(max)
          if int(line[idx]) < min:
              min = int(line[idx])
              print(min)
      checksum = checksum + (max-min)

print (checksum)
