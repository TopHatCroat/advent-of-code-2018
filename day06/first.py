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
infinite_areas = set()

for x in range(max_x + 1):
    for y in range(max_y + 1):
        distances = sorted([ (i, distance(x, y, *p)) for i, p in coords ], key=operator.itemgetter(1))
        if distances[0][1] == distances[1][1]:
            area[x][y] = '.'
        else:
            area[x][y] = distances[0][0]
            point_areas[distances[0][0]] += 1
    
        if x == 0 or x == max_x or y == 0 or y == max_y:
            infinite_areas.add(distances[0][0])

for a in infinite_areas:
    point_areas.pop(a)

print(max(point_areas.items(), key=operator.itemgetter(1))[1])
