SIZE = 100000

def identical_right(snow1: list[int], snow2: list[int], start: int) -> bool:
    for offset in range(6):
        if snow1[offset] != snow2[(start + offset) % 6]:
            return False
    return True

def identical_left(snow1: list[int], snow2: list[int], start: int) -> bool:
    for offset in range(6):
        snow2_index = start - offset
        if snow2_index <= -1:
            snow2_index = snow2_index % 6
        if snow1[offset] != snow2[snow2_index]:
            return False
    return True

def are_identical(snow1: list[int], snow2: list[int]) -> bool:
    for start in range(6):
        if identical_right(snow1, snow2, start):
            return True
        if identical_left(snow1, snow2, start):
            return True
    return False


def identify_identical(snowflakes: list[list[int]], n: int) -> None:
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
    identify_identical(snowflakes, n)

if __name__ == "__main__":
    main()
