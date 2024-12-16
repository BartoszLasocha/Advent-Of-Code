garden = []
with open('12.input', 'r') as f:
    for line in f.readlines():
        garden.append(line.strip())

visited = [[False for _ in range(len(garden[0]))] for _ in range(len(garden))]
perimeters = [[0 for _ in range(len(garden[0]))] for _ in range(len(garden))]
my_new_field = set()

for i in range(len(garden)):
    for j in range(len(garden[i])):
        perimeters[i][j] = 4
        if i > 0 and garden[i-1][j] == garden[i][j]:
            perimeters[i][j] -= 2
        if j > 0 and garden[i][j-1] == garden[i][j]:
            perimeters[i][j] -= 2

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

price = 0
for i in range(len(garden)):
    for j in range(len(garden[i])):
        if not visited[i][j]:
            my_new_field = set()
            my_new_field.add((i, j))
            find_field(i, j)
            perimeter = sum(perimeters[i][j] for (i,j) in my_new_field)
            # print('{}: area {}, perimeter {}'.format(garden[i][j], len(my_new_field), perimeter))
            price += perimeter * len(my_new_field)
print(price)