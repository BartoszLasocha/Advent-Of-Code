import re

with open('03.input', 'r') as f:
    data = f.read()

pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
print(sum(int(match.group(1)) * int(match.group(2)) for match in re.finditer(pattern, data)))
