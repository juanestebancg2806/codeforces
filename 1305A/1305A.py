from sys import stdin

def solve(a,b):
    a.sort(); b.sort()
    print(*a)
    print(*b)


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        stdin.readline()
        a = [int(x) for x in stdin.readline().strip().split()]
        b = [int(x) for x in stdin.readline().strip().split()]
        solve(a,b)


main()

"""
1 5 8
4 5 8


1 5 7
1 2 6
"""