from duplicity.commandline import commands

rules = {}
score = 0

def is_in_order(line):
    ret_val = True
    mistakes = []
    for i in range(len(line)):
        if line[i] in rules:
            if rules[line[i]].intersection(set(line[:i])):
                mistakes.append([line[i], rules[line[i]].intersection(set(line[:i]))])
                ret_val = False
    return ret_val, mistakes

def fix_me(data, mistakes):
    for mistake in mistakes:
        data.remove(mistake[0])
        y = data.index(mistake[1].pop())
        data.insert(y, mistake[0])
    return data

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
        is_ordered, mistakes = is_in_order(data)
        if not is_ordered:
            while not is_ordered:
                data = fix_me(data, mistakes)
                is_ordered, mistakes = is_in_order(data)
            score += data[int(len(data)/2)]
print(score)