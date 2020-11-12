count = [0]
def change_the_switches(switches):
    if count[0] == 0 and len(switches) == 2:
        return max(switches)
    count[0] += 1
    maxim = 0
    maxID = 0
    for i in range(len(switches)):
        if switches[i] > maxim:
            maxim = switches[i]
            maxID = i
        if len(switches) == 1:
            return switches[0]
        elif len(switches) == 2:
            return switches[0] + switches[1]
    if len(switches) == 0:
        return 0
    # print("print", maxim)

    if maxID == 0 or maxID == -1:
        del switches[maxID], switches[maxID]
    else:
        del switches[maxID - 1]
        del switches[maxID - 1]
        del switches[maxID - 1]
    return maxim + change_the_switches(switches)


def main():
    print(change_the_switches([1, 3]))


if __name__ == "__main__":
    main()
