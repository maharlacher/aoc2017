#dayfive_list2

with open("dayfive_list.dat") as input:
    data = input.readlines()

map = [int(val) for val in data]

length = len(map)
location = 0
steps = 0

while location in range(length):
    stepsize = map[location]
    if stepsize > 2:
        map[location] -= 1
    else:
        map[location] += 1    
    location += stepsize
    steps += 1

print steps, location
