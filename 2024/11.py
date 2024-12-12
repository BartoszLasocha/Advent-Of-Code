class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

def generate_linked_list(list):
    root = Element(list[0])
    linked_list = root
    for i in range(1, len(list)):
        linked_list.next = Element(list[i])
        linked_list = linked_list.next
    return root

def print_ll(element):
    print(element.value, end=' ')
    if element.next:
        print_ll(element.next)
    else:
        print()

def len_ll(element):
    length = 1
    while element.next:
        element = element.next
        length += 1
    return length

def blink(linked_list):
    next = None
    if linked_list.value == '0':
        linked_list.value = '1'
        next = linked_list.next
    elif len(linked_list.value) % 2 == 0:
        next = linked_list.next
        value = linked_list.value
        linked_list.value = value[:len(value)//2]
        linked_list.next = Element(str(int(value[len(value)//2:])))
        linked_list.next.next = next
    else:
        linked_list.value = str(2024 * int(linked_list.value))
        next = linked_list.next
    return next

my_ll = None
with open('11.input', 'r') as f:
    my_ll = generate_linked_list(f.read().strip().split(' '))
print_ll(my_ll)

for i in range(75):
    l = my_ll
    while l:
        l = blink(l)
print(len_ll(my_ll))