# It's so disgusting...
# TODO:
# 1. Do not create new map. In fact I only need to place one obstacle, do calculations and remove my new obstacle.
# 2. n^2 for loop is deficient. I prefer to place my obstacle only on original guardian's path.

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


def get_new_trace(rows, x, y, new_x, new_y):
    global state
    if state == rows[x][y]:
        return True
    if rows[x][y] == '.':
        rows[x] = rows[x][:y] + state + rows[x][y + 1:]


def do_shieet(my_tab, x, y, debug=False):
    global state
    my_tab[x] = my_tab[x][:y] + '.' + my_tab[x][y + 1:]
    while 0 <= x < len(rows) and 0 <= y < len(rows[0]):
        if debug:
            print('d ', x, y)
            print(state)
        new_x, new_y = x, y
        if state == '^':
            new_x -= 1
        elif state == 'v':
            new_x += 1
        elif state == '>':
            new_y += 1
        elif state == '<':
            new_y -= 1
        if debug:
            print(state)
            print('dd', new_x, new_y)


        if not (0 <= new_x < len(rows) and 0 <= new_y < len(rows[0])):
            # print('tutaj')
            # print(new_x, new_y)
            return False

        is_in_loop = get_new_trace(my_tab, x, y, new_x, new_y)
        if is_in_loop:
            # print('loop')
            return True
        else:
            # print('not loop')
            pass

        if my_tab[new_x][new_y] == '#':
            if debug:
                for r in my_tab:
                    print(r)
                print()
            if state == '^':
                if debug:
                    print('turn right')
                state = '>'
            elif state == '>':
                if debug:
                    print('turn down')
                state = 'v'
            elif state == 'v':
                if debug:
                    print('turn left')
                state = '<'
            elif state == '<':
                if debug:
                    print('turn up')
                state = '^'
        else:
            x, y = new_x, new_y


result = 0
a = 0
for i in range(len(rows)):
    print(i, '/', len(rows))
    for j in range(len(rows[0])):
        state = '^'
        my_copy = [row[:] for row in rows]
        # if (i != x or j != y) and my_copy[i][j] != '#':
        if i != x or j != y:
            my_copy[i] = my_copy[i][:j] + '#' + my_copy[i][j + 1:]
            debug = False
            if debug:
                for r in my_copy:
                    print(r)
            if do_shieet(my_copy, x, y, debug):
                result += 1
            else:
                a += 1
print(result)
print(a)
# for r in rows:
#     result += r.count('X')
# print(result)

