garden = []
with open('12.input', 'r') as f:
    for line in f.readlines():
        garden.append(line.strip())

visited = [[False for _ in range(len(garden[0]))] for _ in range(len(garden))]
my_new_field = set()


def find_field(i, j):
    global garden, visited, my_new_field
    visited[i][j] = True
    if i > 0 and garden[i][j] == garden[i - 1][j] and not visited[i - 1][j]:
        my_new_field.add((i - 1, j))
        find_field(i - 1, j)

    try:
        if garden[i][j] == garden[i + 1][j] and not visited[i + 1][j]:
            my_new_field.add((i + 1, j))
            find_field(i + 1, j)
    except IndexError:
        pass
    try:
        if garden[i][j] == garden[i][j + 1] and not visited[i][j + 1]:
            my_new_field.add((i, j + 1))
            find_field(i, j + 1)
    except IndexError:
        pass

    if j > 0 and garden[i][j] == garden[i][j - 1] and not visited[i][j - 1]:
        my_new_field.add((i, j - 1))
        find_field(i, j - 1)
    # print(garden[i][j], my_new_field)
    return my_new_field

def calculate_sides(garden_field, by_columns=False):
    # print(garden_field)
    global garden, my_new_field
    sides = 0
    prev_x, prev_y = -1, -1
    if not by_columns:
        is_long_top_side, is_long_bottom_side = False, False
        for (x, y) in garden_field:
            if x != prev_x or y != prev_y + 1:
                is_long_top_side = False
                is_long_bottom_side = False
            # is_top_side = x == 0 or garden[x - 1][y] != garden[x][y]
            is_top_side = x == 0 or (x - 1, y) not in my_new_field
            if not is_top_side:
                is_long_top_side = False
            else:
                if not is_long_top_side:
                    sides += 1
                    # print('top: ', (x, y))
                    is_long_top_side = True
            try:
                # is_bottom_side = garden[x + 1][y] != garden[x][y]
                is_bottom_side = (x + 1, y) not in my_new_field
            except IndexError:
                is_bottom_side = True
            if not is_bottom_side:
                is_long_bottom_side = False
            else:
                if not is_long_bottom_side:
                    sides += 1
                    # print('bottom: ', (x, y))
                    is_long_bottom_side = True
            prev_x = x
            prev_y = y
        return sides
    else:
        is_long_left_side, is_long_right_side = False, False
        prev_x, prev_y = -1, -1
        for (x, y) in garden_field:
            if y != prev_y or x != prev_x + 1:
                is_long_left_side = False
                is_long_right_side = False
            # is_left_side = y == 0 or garden[x][y - 1] != garden[x][y]
            is_left_side = y == 0 or (x, y-1) not in my_new_field
            if not is_left_side:
                is_long_left_side = False
            else:
                if not is_long_left_side:
                    sides += 1
                    # print('left: ', (x, y))
                    is_long_left_side = True
            try:
                # is_right_side = garden[x][y + 1] != garden[x][y]
                is_right_side = (x, y+1) not in my_new_field
            except IndexError:
                is_right_side = True
            if not is_right_side:
                is_long_right_side = False
            else:
                if not is_long_right_side:
                    # print('right: ', (x, y))
                    sides += 1
                    is_long_right_side = True
            prev_y = y
            prev_x = x
        return sides


price = 0
for i in range(len(garden)):
    for j in range(len(garden[i])):
        if not visited[i][j]:
            my_new_field = set()
            my_new_field.add((i, j))
            find_field(i, j)
            sides = calculate_sides(sorted(my_new_field))
            sides += calculate_sides(sorted(my_new_field, key=lambda x: (x[1], x[0])), True)
            print(garden[i][j], sides)
            price += sides * len(my_new_field)
print(price)
