def check_safeness(list_to_check: list, can_remove_element: bool = False) -> bool:
    for i in range(len(list_to_check) - 1):
        if not list_to_check[i] < list_to_check[i + 1] <= (list_to_check[i] + 3):
            if can_remove_element:
                return check_safeness([list_to_check[i]] + list_to_check[i+2:]) or check_safeness(list_to_check[:i] + list_to_check[i+1:])
            else:
                return False
    return True

good = 0
with open('02.input', 'r') as f:
    for line in f.readlines():
        line = [int(i) for i in line.split()]
        if check_safeness(line, True):
            good += 1
        else:
            line.reverse()
            if check_safeness(line, True):
                good += 1
print(good)
