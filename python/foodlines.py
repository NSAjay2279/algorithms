MAX_LINES: int = 100


def shortest_line_index(lines: List[int], n: int) -> int:
    j: int = 1
    shortest: int = 0
    for j in range(n):
        if lines[j] < lines[shortest]:
            shortest = j
    return shortest


def solve(lines: List[int], n: int, m: int) -> None:
    i: int = 0
    shortest: int = 0
    for i in range(m):
        shortest = shortest_line_index(lines, n)
        print(lines[shortest])
        lines[shortest] += 1


def main() -> None:
    lines: List[int] = [0 for _ in range(MAX_LINES)]
    n: int = 0
    m: int = 0
    n, m = list(map(int, input().split()))
    lines = list(map(int, input().split()))
    solve(lines, n, m)


if __name__ == "__main__":
    main()
