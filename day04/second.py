import re
import operator

class SaneDict(dict):
    def __missing__(self, key):
        return 0

with open("input.txt") as f:
    r = re.compile('(\d+|] .*)')
    r2 = re.compile('#\d+')
    lines = []    
    for line in f.readlines():
        stuff = r.findall(line)
        guard = r2.findall(line)
        if guard:
            event = guard[0]
        elif "falls" in stuff[5]:
            event = "s"
        else:
            event = "w"
        
        lines += [[
            int(stuff[0]), 
            int(stuff[1]), 
            int(stuff[2]), 
            int(stuff[3]), 
            int(stuff[4]),
            event
        ]]
    
    lines.sort(key=lambda line: 
        line[4] + line[3] * 60 + line[2] * 60 * 24 + line[1] * 31 * 60 * 24
    )

    when_slept_most = SaneDict()
    iterator = iter(lines)
    current = ''
    for line in iterator:
        if "#" in line[5]:
            current = line[5]
            continue

        for minute in range(line[4], next(iterator)[4]):
            when_slept_most[(current, minute)] += 1

    sleepiest_min = max(when_slept_most.items(), key=operator.itemgetter(1))[0]

    print(int(sleepiest_min[0][1:]) * sleepiest_min[1])    