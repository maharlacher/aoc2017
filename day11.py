# Day 11

string=[]

with open("day11.dat") as input:
  for line in input:
      line = line[0:len(line)-1]
      string.append(line.split(","))

x = 0
y = 0

for step in range(len(string[0])):
    if string[0][step] == "n":
        y += 2
    elif string[0][step] == "ne":
        x += 3
        y += 1
    elif string[0][step] == "se":
        x += 3
        y += -1
    elif string[0][step] == "s":
        y += -2
    elif string[0][step] == "sw":
        x += -3
        y += -1
    elif string[0][step] == "nw":
        x += -3
        y += 1
    else:
        print ("error: bad direction!")

print x,y

if x < 0:
    x = -x
if y < 0:
    y = -y

print x,y

stepsback = 0
while x > 0:
    x += -3
    y += -1
    stepsback += 1

while y > 0:
    y += -2
    stepsback += 1

print x, y, stepsback
