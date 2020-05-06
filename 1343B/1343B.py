from sys import stdin


def solve(n):
    even,odd = list(),list()
    nums = set()
    if((n//2)%2 != 0):
        print("NO")
    else:
        print("YES")
        i,_sum = 2,0
        for _ in range(n//2):
            even.append(i)
            _sum += i
            i += 2
        i = 1
        for k in range(n//2):
            if k+1 == n//2:
                odd.append(_sum)
            else:
                odd.append(i)
            i += 2
            _sum -= odd[-1]
        print(*(even+odd))


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        n = int(stdin.readline().strip())
        solve(n)
main()