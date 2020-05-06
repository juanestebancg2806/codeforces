from sys import stdin


def solve(a,d):
    i,N = 0,len(a)
    while d > 0:
        i = 2
        while i < N and a[1] == 0 and d > 0:
            if a[i] > 0:
                a[1] += 1
                d -= (i-1)
                a[i] -= 1
            i += 1
        if d > 0:
            d -= 1
            if N > 1 and a[1] > 0:
                a[1],a[0] = a[1]-1,a[0]+1
    return a[0]


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n,d = map(int,stdin.readline().strip().split())
        a = [int(x) for x in stdin.readline().strip().split()]
        print(solve(a,d))
main()