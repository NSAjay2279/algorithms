MAX_LINES = 100

shortest_line_index(lines, n):



solve(lines, n, m)


def main():
    lines = [0] * MAX_LINES
    n = 0
    m = 0
    i = 0
    n, m = input().split()
    for i in range(n):
        lines[i] = input()
    solve(lines, n, m)


main()



