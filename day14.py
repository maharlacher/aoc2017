# Day 14 part 1

num_ones = 0

for rows in range (0,128):
    rope = []
    shorthash = []

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
        print row,
        for idx in range(len(row)):
            if row[idx] == "1":
                num_ones += 1
        #print hex(shorthash[outerloop]), bin(shorthash[outerloop]), num_ones
    print

print num_ones
