from sys import stdin


def solve(s):
    ans = i = j = anstmp =  0
    while i < len(s):
        j,anstmp = i+1,0
        if s[i] == '1':
            while j < len(s) and s[j] == '0':
                anstmp,j = anstmp+1,j+1
            if j < len(s) and s[j] == '1':
                ans += anstmp
        i += 1
    return ans

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        s = stdin.readline().strip()
        print(solve(s))

main()