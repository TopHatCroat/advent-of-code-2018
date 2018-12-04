
doubles = 0
triples = 0

with open("input.txt") as f:
    for line in f.readlines():
        counts = [0] * 26
        for ch in line.strip('\n'):
            counts[ord(ch) - 97] += 1

        if 2 in counts:
            doubles += 1
            
        if 3 in counts:
            triples += 1

print(doubles * triples)