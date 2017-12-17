#day seven
string=[]

with open("dayseven.dat") as input:
  for line in input:
      line = line[0:len(line)-1]
      string.append(line.split(" "))

for base in range(len(string)):
    match = False
    for top in range(len(string)):
        for idx in range(3,len(string[top])):    
            if string[base][0] == string[top][idx][0:len(string[base][0])]:
                print string[base][0], string[top][idx][0:len(string[base][0])]
                match = True
    if match == False:
        print string[base][0]
        break
