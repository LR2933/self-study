import sys
def pre_sum(l:list) -> list:
    ret = [0] * (len(l) + 1)
    for i in range(len(l)):
        ret[i + 1] = l[i] + ret[i]
    return ret

def solve():
    data = sys.stdin.read().split()
    nums = list(map(int, data[1:]))
    pre_1 = pre_sum(nums)[1:]
    nums.reverse()
    pre_2 = pre_sum(nums)[1:]
    print(len(set(pre_1) & set(pre_2)))

if __name__ == "__main__":
    solve()
