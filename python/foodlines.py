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


def main():
    lines = [0] * MAX_LINES
    n = 0
    m = 0
    i = 0
    n, m = list(map(int, input().split()))
    people_per_line = list(map(int, input().split()))
    for i in range(n):
        lines[i] = people_per_line[i]
    solve(lines, n, m)


if __name__ == "__main__":
    main()



