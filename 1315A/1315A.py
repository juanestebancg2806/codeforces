from sys import stdin


def solve(a,b,x,y):
    ans = max(x*b,((a-x)-1)*b,y*a,((b-y)-1)*a)
    return ans

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        a,b,x,y = map(int,stdin.readline().strip().split())
        print(solve(a,b,x,y))

main()