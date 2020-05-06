from sys import stdin

def solve(a,b):
    ans = 0
    while a != b:
        if b > a:
            if((b-a)%2 != 0):
                a = a+(b-a)
            else:
                a = b+2
        else:
            if((a-b)%2 == 0):
                a = a-(a-b)
            else:
                a = b-1
        ans += 1
    return ans


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        a,b = map(int,stdin.readline().strip().split())
        print(solve(a,b))
main()