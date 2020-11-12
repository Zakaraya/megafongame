def last_digit(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    return b


def main():
    print(last_digit(10))


if __name__ == "__main__":
    main()
