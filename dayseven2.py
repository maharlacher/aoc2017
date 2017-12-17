#day seven pt2
string=[]

with open("dayseven.dat") as input:
  for line in input:
      line = line[0:len(line)-1]
      string.append(line.split(" "))

#for base in range(len(string)):
#    match = False
#    for top in range(len(string)):
#        for idx in range(3,len(string[top])):
#            if string[base][0] == string[top][idx][0:len(string[base][0])]:
#                print string[base][0], string[top][idx][0:len(string[base][0])]
#                match = True
#    if match == False:
#        print string[base][0]
#        break

def weight(program,lol):
    for node in range(len(lol)):
        if lol[node][0] == program:
            wt = int(lol[node][1][1:len(lol[node][1])-1])
            if len(lol[node]) > 2:
                for idx in range(3,len(lol[node])):
                    word = lol[node][idx]
                    if word[len(word)-1] == ",":
                        word = word[0:len(word)-1]
                    wt += weight(word,lol)
            return wt


for node in range(len(string)):
    if len(string[node]) > 2:
        numtocompare = len(string[node])-4
        word1 = string[node][3]
        if word1[len(word1)-1] == ",":
            word1 = word1[0:len(word1)-1]
        wt1 = weight(word1,string)
        for idx in range(numtocompare):
            word = string[node][4+idx]
            if word[len(word)-1] == ",":
                word = word[0:len(word)-1]
            wtc = weight(word,string)
            if wt1 != wtc:
                print word1, wt1, word, wtc, wt1-wtc

print weight("oxipms",string), weight("ggpau",string), weight("sphbbz",string)
