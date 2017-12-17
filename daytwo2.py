# daytwo_checksum

import csv

checksum = 0

with open("daytwo_input.tsv") as tsv:
  for line in csv.reader(tsv, dialect="excel-tab"):
      num1 = int(line[0])
      num2 = int(line[1])
      for idx1 in range(len(line)-1):
          for idx2 in range(len(line)-idx1-1):
              num1 = float(line[idx1])/float(line[idx2+idx1+1])
              num2 = int(float(line[idx1])/float(line[idx2+idx1+1]))
              if num1 == float(num2):
                  checksum = checksum + int(num1)
                  print (int(line[idx1]),int(line[idx2+idx1+1]),num2,checksum)
              num1 = float(line[idx2+idx1+1])/float(line[idx1])
              num2 = int(float(line[idx2+idx1+1])/float(line[idx1]))
              if num1 == float(num2):
                  checksum = checksum + int(num1)
                  print (int(line[idx1]),int(line[idx2+idx1+1]),num2,checksum)

print (checksum)
