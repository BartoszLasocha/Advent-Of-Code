good = 0

with open('02.input', 'r') as f:
    for line in f.readlines():
        line = [int(i) for i in line.split()]
        if all(line[i] < line[i + 1] <= line[i] + 3 for i in range(len(line) - 1)):
            good += 1
        elif all(line[i + 1] + 3 >= line[i] > line[i + 1] for i in range(len(line) - 1)):
            good += 1
print(good)


