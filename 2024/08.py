antennas = {}
antinodes = set()
debug_antinodes = {}
rows, cols = 0, 0

def calculate_antinode_position(first, last):
    global rows, cols
    results = []
    x = first[0] - (last[0] - first[0])
    y = first[1] - (last[1] - first[1])
    if 0 <= x < cols and 0 <= y < rows:
        results.append((x, y))
    x = last[0] + (last[0] - first[0])
    y = last[1] + (last[1] - first[1])
    if 0 <= x < cols and 0 <= y < rows:
        results.append((x, y))
    return results


with open('08.input', 'r') as f:
    line_number = 0
    file = f.readlines()
    rows = len(file)
    cols = len(file[0]) - 1
    for line in file:
        for i in range(len(line) - 1):
            if line[i] != '.':
                if line[i] in antennas:
                    for position in antennas[line[i]]:
                        for a in calculate_antinode_position((line_number, i), position):
                            antinodes.add(a)
                            if line[i] in debug_antinodes:
                                debug_antinodes[line[i]].add(a)
                            else:
                                debug_antinodes[line[i]] = set()
                                debug_antinodes[line[i]].add(a)
                    antennas[line[i]].append((line_number, i))
                else:
                    antennas[line[i]] = [(line_number, i)]
        line_number += 1
print(antennas)
print(antinodes)
print(debug_antinodes)
print(len(antinodes))

