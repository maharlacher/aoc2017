# dayfour_passphrase2

num_valid = 0

with open("dayfour_passphrase.dat") as input:
  for line in input:
      line = line[0:len(line)-1]
      string = line.split(" ")
      phrase_valid = True
      for idx1 in range(len(string)):
          for idx2 in range(len(string)-idx1-1):
              phrase1 = list(string[idx1])
              phrase2 = list(string[idx2+idx1+1])
              if len(phrase1) == len(phrase2):
                  phrase1.sort()
                  phrase2.sort()
                  if phrase1 == phrase2:
                      phrase_valid = False
                      print phrase1, phrase2
      if phrase_valid:
          num_valid += 1

print num_valid
