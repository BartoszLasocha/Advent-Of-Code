def calc(result, numbers, final):
    if not len(numbers):
        return result == final
    if result > final:
        return False
    return calc(result + numbers[0], numbers[1:], final) or calc(result * numbers[0], numbers[1:], final)


sum = 0
with open('07.input', 'r') as f:
    for line in f.readlines():
        final, my_numbers = line.split(':')
        my_numbers = my_numbers.split()
        final = int(final)
        my_numbers = list(map(int, my_numbers))
        if calc(0, my_numbers, final):
            sum += final
print(sum)