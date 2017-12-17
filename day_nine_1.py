#day nine part 1

score = 0
points = 1
garbage = False
totalgarbage = 0

with open("daynine.dat") as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    if c == "!":
        c = f.read(1)   #read and ignore next character
    elif c == "<":
        garbage = True
        while garbage:
            c = f.read(1)
            if c == "!":
                c = f.read(1)   #read and ignore next character
            elif c == ">":
                garbage = False
            else:
                totalgarbage += 1
    elif c == "{":
        score += points
        points += 1
    elif c == "}":
        points -= 1
    else:               #skip commas and end braces
        print c

print score, totalgarbage
