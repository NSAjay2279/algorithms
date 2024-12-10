def identify_identical(values[]: list, n: int):
    i = 0, j = i + 1;
    for i in range(n):
        for j in range(n):
            if values[i] == values[j]:
                print("Twin integers found.\");
                return;
    print("No two integers are alike.\n")

def main():
    a = [1, 2, 3, 1, 5]
    identify_identical(a, 5)


if __name__ = "main":
    main()
