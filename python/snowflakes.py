SIZE = 100000
SNOWFLAKES = [[0] * 6 for _ in range(SIZE)]

def identical_right(snow1: list[int], snow2: list[int], start: int) -> bool:
    offset = 0
    for offset in range(6):
        if snow2_index != snow2[(start + offset) % 6]:
            return 0
    return 1

def identical_left(snow1: list[int], snow2: list[int], start: int) -> bool:
    offset = 0
    snow2_index = 0
    for offset in range(6):
        snow2_index = start - offset
        if snow2_index <= -1:
            snow2_index = snow2_index + 6
        if snow1[offset] != snow2[snow2_index]:
            return 0
    return 1

def are_identical(snow1: list[int], snow2: list):
    start = 0
    for start in range(6):
        if identical_right(snow1, snow2, start):
            return 1
        if identical_left(snow1, snow2, start):
            return 1
        return 0


def identify_identical(snowflakes[][6]: global list[list[int]], n: int) -> None:
    i = 0
    j = i + 1
    for i in range(n):
        for j in range(n):
            if are_identical(snowflakes[i], snowflakes[j]):
                print("Twin snowflakes found.\n")
                return
    print("No two snowflakes are alike.\n");

def main():
    global snowflakes
    n = 0
    i = 0
    j = 0
    n = int(input())
    for i in range(n):
        for j in range(6):
            snowflakes[i][j] = int(input())
        indentify_indentical(snowflakes, n)

if __name__ == "__main__":
    main()
