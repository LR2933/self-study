import sys
def solve():
    data = list(map(int, sys.stdin.read().split()))

    it = iter(data)
    n, _ = next(it), next(it)
    items = list(zip(it, it)) # value:amount
    items.sort()

    ret = 0
    for v, c in items:
        if c <= n:
            ret += c * v
            n -= c
        else:
            ret += v * n
            n = 0

        if n == 0:
            break

    print(ret)

if __name__ == "__main__":
    solve()
