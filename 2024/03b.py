import re

with open('03.input', 'r') as f:
    data = f.read()

pattern = r"(mul)\(([0-9]{1,3}),([0-9]{1,3})\)|(do)\(\)|(don't)\(\)"

enabled = 1
my_sum = 0
for match in re.finditer(pattern, data):
    if match.group(4) == 'do':
        enabled = 1
    elif match.group(5) == "don't":
        enabled = 0
    else:
        my_sum += enabled * int(match.group(2)) * int(match.group(3))
print(my_sum)