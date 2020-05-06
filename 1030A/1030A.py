from sys import stdin

def main():
    stdin.readline().strip()
    nums = [int(x) for x in stdin.readline().strip().split()]
    print("EASY" if 1 not in nums else "HARD")
main()

