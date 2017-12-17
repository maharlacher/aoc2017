#Day_six.py

bank =[2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
cycles=0
history=[]
keepgoing = True

while keepgoing:
    maxval=0
    for idx in range(len(bank)):
        if bank[idx]>maxval:
            maxidx=idx
            maxval=bank[idx]
    bank[maxidx]=0
    for idx in range(maxval):
        bank[(maxidx+idx+1)%len(bank)] +=1

    for idx in range(len(history)):
        if history[idx]==bank:
            loopstart = idx+1
            keepgoing = False

    history.append(list(bank))
    cycles += 1
    print bank

print loopstart, cycles, (cycles-loopstart)
