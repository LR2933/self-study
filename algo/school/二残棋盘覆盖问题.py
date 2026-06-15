import sys

sys.setrecursionlimit(50000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return []
        
    it = iter(map(int, input_data))
    k = next(it)
    
    size = 2 ** k
    board = [[-1] * (2 ** (k + 1)) for _ in range(size)]
    count = 1

    def helper(start: list, end: list, bad: list):
        nonlocal board, count

        if start[0] == end[0] and start[1] == end[1]:
            return

        mid_x = (start[0] + end[0]) // 2
        mid_y = (start[1] + end[1]) // 2
        
        current_count = count
        count += 1

        if bad[0] <= mid_x:
            if bad[1] <= mid_y:
                board[mid_x][mid_y + 1] = current_count
                board[mid_x + 1][mid_y] = current_count
                board[mid_x + 1][mid_y + 1] = current_count

                helper(start, [mid_x, mid_y], bad)
                helper([start[0], mid_y + 1], [mid_x, end[1]], [mid_x, mid_y + 1])
                helper([mid_x + 1, start[1]], [end[0], mid_y], [mid_x + 1, mid_y])
                helper([mid_x + 1, mid_y + 1], end, [mid_x + 1, mid_y + 1])
            else:
                board[mid_x][mid_y] = current_count
                board[mid_x + 1][mid_y] = current_count
                board[mid_x + 1][mid_y + 1] = current_count

                helper(start, [mid_x, mid_y], [mid_x, mid_y])
                helper([start[0], mid_y + 1], [mid_x, end[1]], bad)
                helper([mid_x + 1, start[1]], [end[0], mid_y], [mid_x + 1, mid_y])
                helper([mid_x + 1, mid_y + 1], end, [mid_x + 1, mid_y + 1])
        else:  
            if bad[1] <= mid_y:
                board[mid_x][mid_y] = current_count
                board[mid_x][mid_y + 1] = current_count
                board[mid_x + 1][mid_y + 1] = current_count

                helper(start, [mid_x, mid_y], [mid_x, mid_y])
                helper([start[0], mid_y + 1], [mid_x, end[1]], [mid_x, mid_y + 1])
                helper([mid_x + 1, start[1]], [end[0], mid_y], bad)
                helper([mid_x + 1, mid_y + 1], end, [mid_x + 1, mid_y + 1])
            else:  
                board[mid_x][mid_y] = current_count
                board[mid_x][mid_y + 1] = current_count
                board[mid_x + 1][mid_y] = current_count

                helper(start, [mid_x, mid_y], [mid_x, mid_y])
                helper([start[0], mid_y + 1], [mid_x, end[1]], [mid_x, mid_y + 1])
                helper([mid_x + 1, start[1]], [end[0], mid_y], [mid_x + 1, mid_y])
                helper([mid_x + 1, mid_y + 1], end, bad)

    left_bad = [next(it), next(it)]
    board[left_bad[0]][left_bad[1]] = 0
    helper([0, 0], [size - 1, size - 1], left_bad)

    right_bad = [next(it), next(it)]
    board[right_bad[0]][right_bad[1]] = 0
    helper([0, size], [size - 1, 2 ** (k + 1) - 1], right_bad)

    for row in board:
        print("\t".join(map(str, row)))

    return board

if __name__ == "__main__":
    solve()
