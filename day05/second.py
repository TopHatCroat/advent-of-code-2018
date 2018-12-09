from string import ascii_lowercase

def react_polymer(polymer):
    stack = []
    for p in polymer.strip('\n'):
        stack += [p]

        while len(stack) >= 2 and stack[-1].lower() == stack[-2].lower() and stack[-1] != stack[-2]:
            stack.pop()
            stack.pop()
    
    return len(stack)

with open("input.txt") as f:
    polymer = f.read()

    results = []
    for char in ascii_lowercase:
        results += [ react_polymer(polymer.replace(char, "").replace(char.upper(), "")) ]

    print(min(results)) 
