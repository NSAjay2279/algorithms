MAX_LINES = 100

def shortest_line_index(lines, n):
    j = 1
    shortest = 0
    for j in range(n):
        if lines[j] < lines[shortest]:
            shortest = j
    return shortest


def solve(lines, n, m):
    i = 0
    shortest = 0
    for i in range(m):
        shortest = shortest_line_index(lines, n)
        print(lines[shortest])
        lines[shortest] += 1


def main():
    n = 0
    m = 0
    i = 0
    n, m = list(map(int, input().split()))
    lines = list(map(int, input().split()))
    solve(lines, n, m)


if __name__ == "__main__":
    main()



