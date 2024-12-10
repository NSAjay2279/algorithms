x = 5

def f():
    global x
    print(x)
    x += 1

def main():
    f()
    f()
    f()

main()
