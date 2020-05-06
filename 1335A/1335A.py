from sys import stdin

def solve(n):
    ans = 0
    if n > 2:
        if(n%2 == 0):
            ans = (n//2)-1
        else:
            ans = n//2
    return ans

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n = int(stdin.readline().strip())
        print(solve(n))


main()
"""
n = 7
6 1
5 2
4 3

n = 8
7 1
6 2
5 3

n = 3
2 1
"""