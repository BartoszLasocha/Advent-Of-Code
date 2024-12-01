left_list = []
right_list = []

with open('01.input', 'r') as f:
    for line in f.readlines():
        left_element, right_element = line.split()
        left_list.append(int(left_element))
        right_list.append(int(right_element))

left_list = sorted(left_list)
right_list = sorted(right_list)

distance = 0
for i in range(len(left_list)):
    distance += abs(left_list[i] - right_list[i])
print(distance)



