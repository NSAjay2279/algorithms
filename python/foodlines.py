MAX_LINES = 100

def shortest_line_index(lines: list, n: int):
    j = 1
    shortest = 0
    for j in range(n):
        if lines[j] < lines[shortest]:
            shortest = j
    return shortest


def solve(lines: list, n: int, m: int):
    i: int = 0
    shortest: int = 0
    for i in range(m):
        shortest = shortest_line_index(lines, n)
        print(lines[shortest])
        lines[shortest] += 1


def main():
    n: int = 0
    m: int = 0
    i: int = 0
    n, m = list(map(int, input().split()))
    lines: int = list(map(int, input().split()))
    solve(lines, n, m)


if __name__ == "__main__":
    main()



