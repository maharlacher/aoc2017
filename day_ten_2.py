# day ten part 2

lengths = []
rope = []
shorthash = []

with open("dayten.dat") as f:
  while True:
    c = f.read(1)
    if c == "\n":
      print "End of file"
      break
    lengths.append(ord(c))

next = len(lengths)
lengths.append(17)
lengths.append(31)
lengths.append(73)
lengths.append(47)
lengths.append(23)

print lengths

for iterations in range(0,256):
    rope.append(iterations)

position = 0
skip = 0

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
    print hex(shorthash[outerloop])
