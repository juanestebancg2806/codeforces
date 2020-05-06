from sys import stdin

def solve(x,y,a,b):
    return -1 if (y-x)%(a+b) != 0 else (y-x)//(a+b)


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        x,y,a,b = map(int,stdin.readline().strip().split())
        print(solve(x,y,a,b))


main()
"""
1)x + (a*m) = z
2)y - (b*m) = z

1) = 2) -> x + (a*m) = y - b*m
(a*m)+(b*m) = y-x
m(a+b) = (y-x)
m = (y-x)/(a+b) -> this is the answer

"""