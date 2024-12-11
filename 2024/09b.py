with open('09.input', 'r') as f:
    text = [int(i) for i in f.read().strip()]
    text = list(map((lambda i: (int(i[1]) * (-1) ** i[0], i[0] // 2, int(i[1]))), enumerate(text)))

def what_to_add(multiplier, length, first_index):
    return multiplier * int((2 * first_index + length - 1) * length / 2)

result = 0
occupied = [0 for i in range(len(text))]
for right_index in range(len(text) - 1, 0, -1):
    if text[right_index][0] > 0:
        new_index = 0
        for left_index in range(0, right_index):
            if text[left_index][0] < 0 and text[left_index][0] + text[right_index][0] <= 0:
                text[left_index] = (text[left_index][0] + text[right_index][0], text[left_index][1], text[left_index][2])
                result += what_to_add(text[right_index][1], text[right_index][0], new_index + occupied[left_index])
                occupied[left_index] += text[right_index][0]
                text[right_index] = (text[right_index][0], 0, text[right_index][2])
                break
            else:
                new_index += text[left_index][2]

new_index = 0
for length, multiplier, basic_length in text:
    if length > 0 and multiplier:
        result += what_to_add(multiplier, length, new_index)
    new_index += basic_length
print(result)