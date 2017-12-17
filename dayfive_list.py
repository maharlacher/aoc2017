#dayfive_list

with open("dayfive_list.dat") as input:
    data = input.readlines()

map = [int(val) for val in data]

length = len(map)
location = 0
steps = 0

while location in range(length):
    map[location] += 1
    location += (map[location]-1)
    steps += 1

print steps, location
