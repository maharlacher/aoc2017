# Day 14 part 2

num_ones = 0
disk = []
line = []

for idx in range(0,130):
    line.append("0")
disk.append(list(line))

for rows in range (0,128):
    print rows
    rope = []
    shorthash = []
    line = "0"

    for iterations in range(0,256):
        rope.append(iterations)

    position = 0
    skip = 0


    lengths = []
    base_input = "ffayrhll-%d"%rows
    #print base_input
    for idx in range(len(base_input)):
        c = base_input[idx]
        lengths.append(ord(c))
    lengths.append(17)
    lengths.append(31)
    lengths.append(73)
    lengths.append(47)
    lengths.append(23)

    #print lengths
    for outerloop in range(0,64):
        for iterations in range(len(lengths)):
            loopcount = 0
            for swap in range(position,position+(lengths[iterations]//2)):
                endidx = (swap+lengths[iterations]-1-(2*loopcount))%256
                temp = rope[swap%256]
                rope[swap%256] = rope[endidx]
                rope[endidx] = temp
                loopcount += 1
            position = (position + lengths[iterations] + skip)%256
            skip += 1

    for outerloop in range(0,16):
        shorthash.append(0)
        for iterations in range(0,16):
            shorthash[outerloop] ^= rope[outerloop*16+iterations]
        #print hex(shorthash[outerloop])
        row = bin(shorthash[outerloop])[2:].zfill(8)
        line = line + str(row)
        for idx in range(len(row)):
            if row[idx] == "1":
                num_ones += 1
        #print hex(shorthash[outerloop]), bin(shorthash[outerloop]), num_ones
    disk.append(list(line+"0"))

line = []
for idx in range(0,130):
    line.append("0")
disk.append(list(line))
regions = 0
max_dimension = 128
min_dimension = 1

def check_adjacent(grid,x,y):
    if x > max_dimension or x < min_dimension:
        return
    if y > max_dimension or y < min_dimension:
        return
    if grid[x+1][y] == "1":
        grid[x+1][y] = "0"
        check_adjacent(grid,x+1,y)
    if grid[x][y+1] == "1":
        grid[x][y+1] = "0"
        check_adjacent(grid,x,y+1)
    if grid[x-1][y] == "1":
        grid[x-1][y] = "0"
        check_adjacent(grid,x-1,y)
    if grid[x][y-1] == "1":
        grid[x][y-1] = "0"
        check_adjacent(grid,x,y-1)
    return

for idx1 in range(1,129):
    for idx2 in range(1,129):
        if disk[idx1][idx2] == "1":
            regions += 1
            disk[idx1][idx2] = chr(0)
            check_adjacent(disk,idx1,idx2)

print regions
