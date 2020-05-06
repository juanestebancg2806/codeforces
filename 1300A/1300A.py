from sys import stdin


def solve(a):
    ans,i,N,psum,nsum = 0,0,len(a),0,0
    for i in range(N):
        ans,a[i] = ans+1 if a[i] == 0 else ans, 1 if a[i] == 0 else a[i]
    
    for i in range(N):
        psum,nsum = psum+a[i] if a[i] >= 0 else psum,nsum+a[i] if a[i] < 0 else nsum
    if(psum == abs(nsum)):
        ans += 1
    return ans


def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        stdin.readline().strip()
        a = [int(x) for x in stdin.readline().strip().split()]
        print(solve(a))
main()