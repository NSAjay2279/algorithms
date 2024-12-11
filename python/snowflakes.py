SIZE = 100000


def match_right(snow1, snow2, start):
    offset = 0
    for offset in range(6):
        if snow1[offset] != snow2[(start + offset) % 6]:
            return False
    return True


def match_left(snow1, snow2, start):
    offset = 0
    index = 0
    for offset in range(6):
        index = start - offset
        if snow2_index <= -1:
            index = index % 6
        if snow1[offset] != snow2[index]:
            return False
    return True


def are_identical(snow1: list[int], snow2: list[int]):
    start = 0
    for start in range(6):
        if match_right(snow1, snow2, start):
            return True
        if match_left(snow1, snow2, start):
            return True
    return False


def find_twins(snowflakes: List[List[int]], n):
    i = 0
    j = 0
    for i in range(n):
        for j in range(i+1, n):
            if are_identical(snowflakes[i], snowflakes[j]):
                print("Twin snowflakes found.\n")
                return
    print("No two snowflakes are alike.\n");

def main():
    snowflakes = [[0] * 6 for _ in range(SIZE)]
    n = 0
    n = int(input())
    snowflakes = [list(map(int, input().split())) for _ in range(n)]
    find_twins(snowflakes, n)

if __name__ == "__main__":
    main()
