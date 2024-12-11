rows = []
x, y = 0, 0
state = '^'  # < v >

with open('06.input', 'r') as f:
    k = -1
    for line in f.readlines():
        line = line[:-1]
        rows.append(line)
        k += 1
        try:
            y = line.index(state)
            print(k, y)
            x = k
        except ValueError:
            continue
print(rows)

while 0 <= x < len(rows) and 0 <= y < len(rows[0]):
    rows[x] = rows[x][:y] + 'X' + rows[x][y+1:]
    new_x, new_y = x, y
    if state == '^':
        new_x -= 1
    elif state == 'v':
        new_x += 1
    elif state == '>':
        new_y += 1
    elif state == '<':
        new_y -= 1
    print(new_x, new_y)

    if not (0 <= new_x < len(rows) and 0 <= new_y < len(rows[0])):
        break

    if rows[new_x][new_y] == '#':
        if state == '^':
            state = '>'
        elif state == '>':
            state = 'v'
        elif state == 'v':
            state = '<'
        elif state == '<':
            state = '^'
    else:
        x, y = new_x, new_y

result = 0
for r in rows:
    result += r.count('X')
print(result)
