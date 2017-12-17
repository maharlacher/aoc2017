# Day 17

step_size = 304    # puzzle input

position = 0
spinlock = [0]
steps = 0

while steps < 2017:
    steps += 1
    position = ((position + step_size) % len(spinlock)) + 1
    spinlock.insert(position,steps)

for steps in range(len(spinlock)):
    if (spinlock[steps] == 2017):
        print "answer is: ", spinlock[steps+1]
