from sys import stdin


def solve(a: list) -> bool:
    ans,_sum,odd,even = True,sum(a),0,0
    if _sum%2 == 0:
        for i in range(len(a)):
            odd = odd+1 if a[i]%2 != 0 else odd
            even = even+1 if a[i]%2 == 0 else even
        if odd == 0 or (odd%2 == 0 and even == 0): ans = False

    return ans

def main() -> None:
    t = int(stdin.readline().strip())
    for _ in range(t):
        stdin.readline()
        a = [int(x) for x in stdin.readline().strip().split()]
        print("YES" if solve(a) else "NO")

main()
"""
[2,3,5]

"""