# Day 17 part 2

step_size = 304    # puzzle input

position = 0
spinlock = [0]
steps = 0

while steps < 50000000:
    steps += 1
    position = ((position + step_size) % len(spinlock)) + 1
    spinlock.insert(position,steps)

steps = 0
stop = len(spinlock)

while steps < stop:
    if (spinlock[steps] == 0):
        print "answer is: ", spinlock[steps+1]
    steps += 1
