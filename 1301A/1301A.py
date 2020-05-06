from sys import stdin


def solve(a,b,c):
    ans,i,N = True,0,len(a)
    while i < N and ans:
        ans,i = (c[i] == a[i]) or(c[i] == b[i]),i+1
    return ans

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        a = stdin.readline().strip()
        b = stdin.readline().strip()
        c = stdin.readline().strip()
        print("YES" if solve(a,b,c) else "NO")
main()
