from functools import reduce
from operator import mul

WIDTH = 101
HEIGHT = 103
SECONDS = 100
counts = [0] * 4
with open('14.input', 'r') as f:
    for robot_line in f.readlines():
        position, movement = robot_line.strip().split(' ')
        position = list(map(int, position.split('=')[1].split(',')))
        movement = [x * SECONDS for x in list(map(int, movement.split('=')[1].split(',')))]
        position = [(position[0] + movement[0]) % WIDTH, (position[1] + movement[1]) % HEIGHT]
        if position[0] > WIDTH // 2:
            if position[1] > HEIGHT // 2:
                counts[0] += 1
            elif position[1] < HEIGHT // 2:
                counts[1] += 1
        elif position[0] < WIDTH // 2:
            if position[1] > HEIGHT // 2:
                counts[2] += 1
            elif position[1] < HEIGHT // 2:
                counts[3] += 1
print(reduce(mul, counts))


