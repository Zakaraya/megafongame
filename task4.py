def change_the_switches(switches):
    even = []
    odd = []
    for item in range(len(switches)):
        if item % 2 == 0:
            even.append(switches[item])
        else:
            odd.append(switches[item])
    if sum(even) > sum(odd):
        return sum(even)
    return sum(odd)


def main():
    a = [2, 7, 9, 3, 1]
    print(change_the_switches(a))


if __name__ == "__main__":
    main()
