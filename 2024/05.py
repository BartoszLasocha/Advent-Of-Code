from duplicity.commandline import commands

rules = {}
score = 0

def is_in_order(line):
    for i in range(len(line)):
        if line[i] in rules:
            if rules[line[i]].intersection(set(line[:i])):
                return False
    return True

with open('05.input', 'r') as f:
    reader = f
    try:
        for line in reader:
            key, val = line.split('|')
            if int(key) in rules:
                rules[int(key)].add(int(val))
            else:
                rules[int(key)] = {int(val)}
    except ValueError:
        pass
    for line in reader:
        data = [int(x) for x in line.split(',')]
        if is_in_order(data):
            score += data[int(len(data)/2)]
print(score)