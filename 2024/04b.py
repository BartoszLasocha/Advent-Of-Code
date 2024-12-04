with open('04.input', 'r') as f:
    data = f.read().splitlines()

max_row = len(data) - 1
max_column = len(data[0]) - 1

def find_xmas(row, column):
    if row == 0 or column == 0 or row == max_row or column == max_column:
        return 0
    if (data[row-1][column-1] == 'M' and data[row+1][column+1] == 'S') or (data[row-1][column-1] == 'S' and data[row+1][column+1] == 'M'):
        if (data[row-1][column+1] == 'M' and data[row+1][column-1] == 'S') or (data[row-1][column+1] == 'S' and data[row+1][column-1] == 'M'):
            return 1
    return 0

xmas_count = 0
for row in range(len(data)):
    for column in range(len(data[row])):
        if data[row][column] == 'A':
            xmas_count += find_xmas(row, column)
print(xmas_count)
