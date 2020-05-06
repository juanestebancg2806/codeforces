from sys import stdin


def main():
    t =  int(stdin.readline().strip())
    for _ in range(t):
        n,m = map(int,stdin.readline().strip().split())
        print("YES" if n%m == 0 else "NO")

main()