# day ten part 1

lengths = [120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113]
rope = []

for iterations in range(0,256):
    rope.append(iterations)

position = 0
skip = 0

for iterations in range(len(lengths)):
    loopcount = 0
    for swap in range(position,position+(lengths[iterations]//2)):
        endidx = (swap+lengths[iterations]-1-(2*loopcount))%256
        print swap%256, endidx
        temp = rope[swap%256]
        rope[swap%256] = rope[endidx]
        rope[endidx] = temp
        loopcount += 1
    position = (position + lengths[iterations] + skip)%256
    skip += 1
    print rope

print rope[0]*rope[1]
