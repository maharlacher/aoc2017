# day 8 part 1

registers = [[0,0],[0,0]]
firstpass = True
maxever = 0

def incdec(register,command):
    if command[1] == "inc":
        value = register + int(command[2])
    else:
        value = register - int(command[2])
    return value

with open("dayeight.dat") as input:
  for line in input:
      line = line[0:len(line)-1]
      string = line.split(" ")
      inlist1 = inlist2 = False
      if firstpass:
          firstpass = False
          registers[0][0] = string[0]
          registers[1][0] = string[4]
      for idx in range(len(registers)):
          if string[0] == registers[idx][0]:
              inlist1 = True
              firstreg = idx
          if string[4] == registers[idx][0]:
              inlist2 = True
              secondreg = idx
      if inlist1 == False:
          firstreg = len(registers)
          registers.append([string[0],0])
      if inlist2 == False:
          if string[4] != string[0]:    #make sure it is still false
              secondreg = len(registers)
              registers.append([string[4],0])

      if string[5] == "==":
          if registers[secondreg][1] == int(string[6]):
              registers[firstreg][1] = incdec(registers[firstreg][1],string)
      elif string[5] == ">":
          if registers[secondreg][1] > int(string[6]):
              registers[firstreg][1] = incdec(registers[firstreg][1],string)
      elif string[5] == ">=":
          if registers[secondreg][1] >= int(string[6]):
              registers[firstreg][1] = incdec(registers[firstreg][1],string)
      elif string[5] == "<":
          if registers[secondreg][1] < int(string[6]):
              registers[firstreg][1] = incdec(registers[firstreg][1],string)
      elif string[5] == "<=":
          if registers[secondreg][1] <= int(string[6]):
              registers[firstreg][1] = incdec(registers[firstreg][1],string)
      elif string[5] == "!=":
          if registers[secondreg][1] != int(string[6]):
              registers[firstreg][1] = incdec(registers[firstreg][1],string)
      else:
          print("error: unrecognized evaluation: ", string[5])
      if registers[firstreg][1] > maxever:
          maxever = registers[firstreg][1]

max = 0
maxreg = 0
for idx in range(len(registers)):
    if registers[idx][1] > max:
        max = registers[idx][1]
        maxreg = idx

print registers
print registers[maxreg][0], maxever
