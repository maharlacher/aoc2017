# Day 13 part 2

walls = []

with open("day13.dat") as input:
  for line in input:
      walls.append(line.split(" "))

for idx in range(len(walls)):
    walls[idx][0] = int(walls[idx][0][0:len(walls[idx][0])-1])
    walls[idx][1] = int(walls[idx][1][0:len(walls[idx][1])-1])

delay = 139655
go = True
length = len(walls)

while go:
    go = False
    delay += 1
    severity = 0
    next = 0
    while next < length:
        if (walls[next][0]+delay)%(2*walls[next][1]-2) == 0:
            severity += walls[next][0]*walls[next][1]
            go = True
        next += 1

print delay
