#Kristen Ching
start = int(input("Please enter your starting number: "))
size = int(input("Please enter your sequence size: "))
seq = []
for x in range(0, size):
    seq.append("")
    seq[x] = int(seq[x])
output = 0
for x in range(0, size):
    if x == 0 or x == 1:
        seq[x] = start
    else:
        seq[x] = (seq[x-2] + seq[x-1])
        output = output + intseq[x] + " "
