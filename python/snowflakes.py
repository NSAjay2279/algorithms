def identify_identical(values: list, n: int):
    i = 0
    j = 1
    for i in range(n):
        for j in range(n):
            if values[i] == values[j]:
                print("Twin integers found.\n");
                return;
    print("No two integers are alike.\n")

def identical_right(snow1: list, snow2: list, start: int):
    offset = 0
    for offset in range(6):
        if snow1[offset] != snow2[start + offset]:
            return False
    return True




if __name__ == "__main__":
    main()
