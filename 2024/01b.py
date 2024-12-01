left_list = []
right_dict = {}

with open('./01.input', 'r') as f:
    for line in f.readlines():
        left_element, right_element = line.split()
        left_list.append(int(left_element))
        right_element = int(right_element)
        if right_element in right_dict:
            right_dict[right_element] += 1
        else:
            right_dict[right_element] = 1

distance = 0
for left_element in left_list:
    distance += left_element * right_dict.get(left_element, 0)
print(distance)


