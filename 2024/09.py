with open('09.input', 'r') as f:
    number_text = f.read().strip()
    is_dot = False
    text = []
    i = 0
    for number in number_text:
        if is_dot:
            for _ in range(int(number)):
                text.append('.')
        else:
            for _ in range(int(number)):
                text.append(str(i))
            i += 1
        is_dot = not is_dot
    print(text)

    i, j = 0, len(text) - 1
    result_sum = 0
    while i <= j:
        if text[i] != '.':
            result_sum += int(text[i]) * i
            print(i, int(text[i]) * i)
        else:
            while text[j] == '.':
                j -= 1
            result_sum += int(text[j]) * i
            print(i, int(text[j]) * i, '_')
            j -= 1
        i += 1
print(result_sum)
