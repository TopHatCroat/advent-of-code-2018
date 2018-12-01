import cProfile

from typing import List

def find_double_freq(input: List[str]) -> int:
    alreadySeen = {}
    result = 0

    while True:
        for line in input:
            if line[:1] == '+':
                result += int(line[1:])
            elif line[:1] == '-':
                result -= int(line[1:])
            else:
                raise ValueError("{} must start with either '+' or '-'")

            if alreadySeen.get(result, False):
                return result
            else:
                alreadySeen[result] = True
                
with open("input.txt") as f:
    result = find_double_freq(f.readlines())
    print(result)
