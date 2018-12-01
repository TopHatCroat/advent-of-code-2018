
result = 0

with open("input.txt") as f:
    for line in f.readlines():
        if line[:1] == '+':
            result += int(line[1:])
        elif line[:1] == '-':
            result -= int(line[1:])
        else:
            raise ValueError("{} must start with either '+' or '-'".format(line))

print(result)
