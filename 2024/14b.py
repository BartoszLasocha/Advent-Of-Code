
WIDTH = 101
HEIGHT = 103

positions = []
movements = []
positions_set = ()

TEST_SETS = []
for i in range(HEIGHT//2 - 2 , HEIGHT//2 + 3):
    test_set = set()
    for j in range((WIDTH+2)//2 - 2, (WIDTH+2)//2 + 3):
        test_set.add((j, i))
    TEST_SETS.append(test_set)


def print_tab():
    global positions_set
    print('-' * WIDTH)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (j, i) in positions_set:
                print('X', end='')
            else:
                print(' ', end='')
        print()
    print('-' * WIDTH)

with open('14.input', 'r') as f:
    for robot_line in f.readlines():
        position, movement = robot_line.strip().split(' ')
        positions.append(list(map(int, position.split('=')[1].split(','))))
        movements.append(list(map(int, movement.split('=')[1].split(','))))

print(positions)
print(movements)
print(TEST_SETS)
moves = 0
while True:
    positions = [((positions[i][0] + movements[i][0]) % WIDTH, (positions[i][1] + movements[i][1]) % HEIGHT) for i in range(len(positions))]
    positions_set = set(positions)
    moves += 1
    if any(positions_set.issuperset([(x, i) for x in range(WIDTH//2 - 2, WIDTH//2 + 3)]) for i in range(HEIGHT)):
        print_tab()
        print(moves)
        input()
