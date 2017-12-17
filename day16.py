# Day 16

dance=[]
positions=[]

with open("day16.dat") as input:
  for line in input:
      line = line[0:len(line)-1]
      dance.append(line.split(","))

firstchar = "a"

for idx in range (0,16):
    positions.append(firstchar)
    firstchar = chr(ord(firstchar) + 1)

start_position = list(positions)

moves = 0
total_steps = len(dance[0])

while moves < 1000000000:
    moves += 1
    idx = 0
    while idx < total_steps:
        if dance[0][idx][0] == "s":
            spin = int(dance[0][idx][1:])
            temp = positions
            positions = positions[16-spin:]
            for idx2 in range(0,16-spin):
                positions.append(temp[idx2])
        elif dance[0][idx][0] == "x":
            xchange = []
            xchange.append(dance[0][idx].split("/"))
            x1 = int(xchange[0][0][1:])
            x2 = int(xchange[0][1])
            temp = positions[x1]
            positions[x1] = positions[x2]
            positions[x2] = temp
        elif dance[0][idx][0] == "p":
            xchange = []
            xchange.append(dance[0][idx].split("/"))
            p1 = xchange[0][0][1:]
            p2 = xchange[0][1]
            idx2 = 0
            while idx2 < 16:
                if positions[idx2] == p1:
                    x1 = idx2
                elif positions[idx2] == p2:
                    x2 = idx2
                idx2 += 1
            temp = positions[x1]
            positions[x1] = positions[x2]
            positions[x2] = temp
        idx += 1
    if (positions == start_position):
        print moves, ": ", positions
        moves = 1000000000 - (1000000000 % moves)
        #moves = 1000000000 % moves

print positions
