def calc(result, numbers, final):
    if not len(numbers):
        return result == final
    if result > final:
        return False
    number = int(numbers[0])
    return (calc(result + number, numbers[1:], final)
            or calc(result * number, numbers[1:], final)
            or calc(int(str(result) + numbers[0]), numbers[1:], final))

sum = 0
with open('07.input', 'r') as f:
    for line in f.readlines():
        final, my_numbers = line.split(':')
        my_numbers = my_numbers.split()
        final = int(final)
        if calc(0, my_numbers, final):
            sum += final
print(sum)