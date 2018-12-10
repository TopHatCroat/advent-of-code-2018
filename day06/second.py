import re
import operator

class SaneDict(dict):
    def __missing__(self, key):
        return 0


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

r = re.compile('\d+')
coords = [ list(map(int, r.findall(line))) for line in open("input.txt").readlines() ]
max_x = max(map(lambda x: x[0], coords))
max_y = max(map(lambda x: x[1], coords))
coords = [ (i, coord) for i, coord in enumerate(coords) ]

area = [ ['-'] * (max_y + 1) ] * ( max_x + 1)
point_areas = SaneDict()

region_size = 0

for x in range(max_x + 1):
    for y in range(max_y + 1):  
        total_dist = sum([ distance(x, y, *p) for i, p in coords ])
        if total_dist < 10000:
            region_size += 1


print(region_size)
