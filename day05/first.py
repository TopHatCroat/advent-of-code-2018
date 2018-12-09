
with open("input.txt") as f:
    polymer = f.read()
    stack = []
    for p in polymer.strip('\n'):
        stack += [p]

        while len(stack) >= 2 and stack[-1].lower() == stack[-2].lower() and stack[-1] != stack[-2]:
            stack.pop()
            stack.pop()

    print(len(stack)) 
