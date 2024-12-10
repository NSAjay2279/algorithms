SIZE = 100000
SNOWFLAKES = [[0] * 6 for _ in range(SIZE)]

def identical_right(snow1: list[int], snow2: list[int], start: int) -> bool:
    offset = 0
    for offset in range(6):
        if snow1[offset] != snow2[(start + offset) % 6]:
            return False
    return True

def identical_left(snow1: list[int], snow2: list[int], start: int) -> bool:
    offset = 0
    snow2_index = 0
    for offset in range(6):
        snow2_index = start - offset
        if snow2_index <= -1:
            snow2_index = snow2_index % 6
        if snow1[offset] != snow2[snow2_index]:
            return False
    return True

def are_identical(snow1: list[int], snow2: list[int]) -> bool:
    start = 0
    for start in range(6):
        if identical_right(snow1, snow2, start):
            return True
        if identical_left(snow1, snow2, start):
            return 1
    return False


def identify_identical(snowflakes: list[list[int]], n: int) -> None:
    i = 0
    j = i + 1
    for i in range(n):
        for j in range(n):
            if are_identical(snowflakes[i], snowflakes[j]):
                print("Twin snowflakes found.\n")
                return
    print("No two snowflakes are alike.\n");

def main():
    n = 0
    i = 0
    j = 0
    n = int(input())
    snowflakes = list(map(int, input().split()))
    identify_identical(snowflakes, n)

if __name__ == "__main__":
    main()
