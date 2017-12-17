# dayfour_passphrase

num_valid = 0

with open("dayfour_passphrase.dat") as input:
  for line in input:
      line = line[0:len(line)-1]
      string = line.split(" ")
      phrase_valid = True
      for idx1 in range(len(string)):
          for idx2 in range(len(string)-idx1-1):
              if string[idx1] == string[idx2+idx1+1]:
                  phrase_valid = False
      if phrase_valid:
          print string
          num_valid += 1

print num_valid
