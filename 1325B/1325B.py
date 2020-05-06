from sys import stdin



def solve(a):
    a = list(set(a))
    return len(a)

def main():
    t = int(stdin.readline().strip())
    for _ in range(t):
        stdin.readline()
        a = [int(x) for x in stdin.readline().strip().split()]
        print(solve(a))


main()
"""
[3,2,1] -> [3,2,1,3,2,1,3,2,1]
[3,1,4,1,5,9] -> [3,1,4,1,5,9,3,1,4,1,5,9,3,1,4,1,5,9,3,1,4,1,5,9,3,1,4,1,5,9,3,1,4,1,5,9]

"""