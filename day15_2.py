# Day 15 part 2

a_fact = 16807
b_fact = 48271

divider = 2147483647

a = 618
b = 814

results_a = []
results_b = []

itera = 0
iterb = 0
count = 0

while (itera < 5000000):

    a = (a * a_fact) % divider

    if a % 4 == 0:
        bina = bin(a)[2:].zfill(32)
        results_a.append(bina[16:])
        itera += 1

print ("a is done!")

while (iterb < 5000000):

    b = (b * b_fact) % divider

    if b % 8 == 0:
        binb = bin(b)[2:].zfill(32)
        results_b.append(binb[16:])
        iterb += 1

print ("b is done too!")

iterations = 0

while iterations < 5000000:
    if results_a[iterations] == results_b[iterations]:
        print ("match on iteration: "),iterations
        count += 1
    iterations += 1
    
print count
