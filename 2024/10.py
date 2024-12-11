topographic_map = []
possible_ends = {}


with open('10.input', 'r') as f:
    topographic_map = [line.strip() for line in f.readlines()]
    print(topographic_map)

def find_path(start_x, start_y, x=0, y=0):
    if topographic_map[y][x] == '9':
        possible_ends[start_x + start_y].add(str(x) + str(y))
        return
    try:
        if int(topographic_map[y+1][x]) - 1 == int(topographic_map[y][x]):
            find_path(start_x, start_y, x, y+1)
    except IndexError:
        pass
    if y > 0 and int(topographic_map[y-1][x]) - 1 == int(topographic_map[y][x]):
        find_path(start_x, start_y, x, y-1)

    try:
        if int(topographic_map[y][x+1]) - 1 == int(topographic_map[y][x]):
            find_path(start_x, start_y, x+1, y)
    except IndexError:
        pass
    if x > 0 and int(topographic_map[y][x-1]) - 1 == int(topographic_map[y][x]):
        find_path(start_x, start_y, x-1, y)


for y in range(len(topographic_map)):
    for x in range(len(topographic_map[y])):
        if int(topographic_map[y][x]) == 0:
            possible_ends[str(x) + str(y)] = set()
            find_path(str(x), str(y), x, y)

print(sum(len(x) for x in possible_ends.values()))