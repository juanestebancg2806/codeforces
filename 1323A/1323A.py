from sys import stdin

def solve(a):
    ans = False
    i = j = 0
    while i < len(a) and not ans:
        ans = a[i]%2 == 0
        if ans:
            print(1)
            print(i+1)
        i += 1
    i = 0
    while i < len(a) and not ans:
        j = i+1
        while j < len(a) and not ans:
            ans = (a[i]+a[j])%2 == 0
            if(ans):
                print(2)
                print(i+1,j+1)
            j += 1
        i += 1
    if not ans:
        print(-1)

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        stdin.readline()
        a = [int(x) for x in stdin.readline().strip().split()]
        solve(a)

main()