import sys

def solve():
    input_data = list(map(int, sys.stdin.read().split()))
    if not input_data:
        return
        
    n, w = input_data[:2]
    nums = input_data[2:]
    ret1 = 0
    ret2 = [0] * n

    def helper(current: int, count: list):
        nonlocal ret1, ret2

        if current > w:
            return
        if current > ret1:
            ret1 = current
            ret2 = count
        if len(count) == n:
            return

        i = len(count)
        helper(current + nums[i], count + [1])
        helper(current, count + [0])

    helper(0, [])

    print(ret1)
    print(*ret2)

if __name__ == "__main__":
    solve()
