from sys import stdin


def solve(a,m):
    ans,_sum = a[0],sum(a[1:])
    if len(a) > 1:
        ans = min(m,a[0]+_sum)
    return ans

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n,m = map(int,stdin.readline().strip().split())
        a = [int(x) for x in stdin.readline().strip().split()]
        print(solve(a,m))

main()