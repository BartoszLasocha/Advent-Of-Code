with open('04.input', 'r') as f:
    data = f.read().splitlines()

def find_xmas(row, column):
    # Add first letter
    strings_to_search = ['X' for _ in range(9)]
    # Add remaining letters
    for inc in range(1, 4):
        k = -1
        for i in range(row-inc, row+inc+1, inc):
            for j in range(column-inc, column+inc+1, inc):
                if i != row or j != column:
                    k += 1
                    try:
                        if i < 0 or j < 0:
                            continue
                        strings_to_search[k] += data[i][j]
                    except IndexError:
                        continue
    found = 0
    for word in strings_to_search:
        if word == 'XMAS':
            found += 1
    return found

xmas_count = 0
for row in range(len(data)):
    for column in range(len(data[row])):
        if data[row][column] == 'X':
            xmas_count += find_xmas(row, column)
print(xmas_count)
