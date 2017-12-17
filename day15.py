# Day 15

a_fact = 16807
b_fact = 48271

divider = 2147483647

a = 618
b = 814

iterations = 0
count = 0

while iterations < 40000000:
    iterations += 1
    a = (a * a_fact) % divider
    b = (b * b_fact) % divider

    bina = bin(a)[2:].zfill(32)
    binb = bin(b)[2:].zfill(32)

    if bina[16:] == binb[16:]:
        print ("match on iteration: "),iterations
        count += 1

print count
