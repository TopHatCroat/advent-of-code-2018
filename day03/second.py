import re

class SaneDict(dict):
    def __missing__(self, key):
        return []

with open("input.txt") as f:
    area = SaneDict()
    r = re.compile('\d+')
    lines = [ list(map(int, r.findall(line))) for line in f.readlines() ]
    for line in lines:
        for x in range(line[1], line[1] + line[3]):
            for y in range(line[2], line[2] + line[4]):
                area[(x, y)] += [line[0]]


    collision_areas = {}
    for pos, claims in area.items():
        if len(claims) >= 2:
            for id in claims: 
                collision_areas[id] = True 

    for not_collided in filter(lambda line: not collision_areas.get(line[0], False), lines):
        print(not_collided)
