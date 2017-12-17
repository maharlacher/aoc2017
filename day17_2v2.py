# Day 17 part 2 - shortcut version?

step_size = 304    # puzzle input

position = 0
spinlock = [0]
steps = 0

while steps < 50000000:
    steps += 1
    position = ((position + step_size) % steps) + 1
    if position == 1:
        print steps


print "answer is: ", spinlock[1]
