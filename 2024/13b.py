import re
from sympy import symbols, Eq, solve

def parse_xy(line):
    return list(map(int, re.match('.*X[/+=](\d+).*Y[/+=](\d+).*', line).groups()))

with open('13.input', 'r') as f:
    p = True
    price = 0
    while p:
        a = f.readline().strip()
        b = f.readline().strip()
        p = f.readline().strip()
        f.readline()
        if p:
            a = parse_xy(a)
            b = parse_xy(b)
            p = parse_xy(p)
            p[0] += 10000000000000
            p[1] += 10000000000000

            sa, sb = symbols('a b')
            e1 = Eq(a[0] * sa + b[0] * sb, p[0])
            e2 = Eq(a[1] * sa + b[1] * sb, p[1])
            sol = solve((e1, e2), (sa, sb))
            sa, sb = int(sol[sa]), int(sol[sb])
            if sa * a[0] + sb * b[0] == p[0] and sa * a[1] + sb * b[1] == p[1]:
                price += sa * 3 + sb
print(price)