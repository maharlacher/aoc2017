# Day 13 part 1

walls = []

with open("day13.dat") as input:
  for line in input:
      walls.append(line.split(" "))

for idx in range(len(walls)):
    walls[idx][0] = int(walls[idx][0][0:len(walls[idx][0])-1])
    walls[idx][1] = int(walls[idx][1][0:len(walls[idx][1])-1])

print walls

severity = 0

for next in range(len(walls)):
    if walls[next][0]%(2*walls[next][1]-2) == 0:
        severity += walls[next][0]*walls[next][1]
        print walls[next][0], severity
