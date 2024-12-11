MAX_LINES = 100


def min_idx(lines, n):
    j = 1
    min_idx = 0
    for j in range(n):
        if lines[j] < lines[min_idx]:
            min_idx = j
    return min_idx


def solve(lines, n, m):
    i = 0
    min_idx = 0
    for i in range(m):
        min_idx_val = min_idx(lines, n)
        print(lines[min_idx_val])
        lines[min_idx_val] += 1


def main():
    lines = [0 for _ in range(MAX_LINES)]
    n = 0
    m = 0
    n, m = list(map(int, input().split()))
    lines = list(map(int, input().split()))
    solve(lines, n, m)


if __name__ == "__main__":
    main()



