#day 12 part 2
pipes = []

with open("day12.dat") as input:
  for line in input:
      pipes.append(line.split(" "))

prog_list = []
groups = 0

def follow_pipe(prog_list,idx,pipes):
    for prog in range(len(pipes[idx])):
        if (prog == 0) and (pipes[idx][0] not in prog_list):
            prog_list.append(pipes[idx][0])
        elif (prog > 1):
            if pipes[idx][prog][0:len(pipes[idx][prog])-1] not in prog_list:
                prog_list.append(pipes[idx][prog][0:len(pipes[idx][prog])-1])
                follow_pipe(prog_list,int(pipes[idx][prog][0:len(pipes[idx][prog])-1]),pipes)

for idx in range (len(pipes)):
    if pipes[idx][0] not in prog_list:
        follow_pipe(prog_list,idx,pipes)
        groups += 1

print prog_list
print len(prog_list)
print groups
