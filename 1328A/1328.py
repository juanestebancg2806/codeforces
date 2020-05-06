from sys import stdin

def f(b,x):
    return b*x

def binarySearch(a,b):
    lo,hi,mid = 0,(10**9)+1,0
    while lo+1 != hi:
        mid = (lo+hi)>>1
        if(f(b,mid) <= a):
            lo = mid
        else:
            hi = mid
    return hi


def solve(a,b):
    ans = None
    if a%b == 0:
        ans = 0
    elif b > a:
        ans = b-a
    else:
        x = binarySearch(a,b)
        ans = abs((b*x)-a)
    return ans


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        a,b = map(int,stdin.readline().strip().split())
        print(solve(a,b))

main()

"""
-> ((a+x) mod b) = 0


"""