my_list = []
total_length = 0

BLINK_DEPTH = 75

level_sets = [set() for _ in range(BLINK_DEPTH + 1)]

def blink(element):
    if element == '0':
        return ['1']
    elif len(element) % 2 == 0:
        value = element
        return [value[:len(value)//2], str(int(value[len(value)//2:]))]
    else:
        return [str(2024 * int(element))]

def blink_iter(set_to_blink):
    new_set = set()
    for element in set_to_blink:
        new = blink(element)
        for new_element in new:
            new_set.add(new_element)
    return new_set

with open('11.input', 'r') as f:
    my_list = f.read().strip().split(' ')

level_sets[0] = set(my_list)
for i in range(1, BLINK_DEPTH + 1):
    level_sets[i] = blink_iter(level_sets[i-1])

total_level = [{} for _ in range(BLINK_DEPTH + 1)]
total_level[BLINK_DEPTH] = {k: 1 for k in level_sets[BLINK_DEPTH]}
for i in range(BLINK_DEPTH - 1, -1, -1):
    for element in level_sets[i]:
        if element == '0':
            total_level[i][element] = total_level[i + 1]['1']
        elif len(element) % 2 == 0:
            total_level[i][element] = total_level[i + 1][element[:len(element) // 2]] + total_level[i + 1][str(int(element[len(element) // 2:]))]
        else:
            total_level[i][element] = total_level[i + 1][str(2024 * int(element))]
print(sum(total_level[0].values()))
