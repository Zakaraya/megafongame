def check_availability(schedule, current_time):
    start_arr = {}
    end_arr = []
    for interval in range(len(schedule)):
        start_arr[interval] = schedule[interval].split('-')
    for sublist in start_arr.values():
        for item in sublist:
            if item not in end_arr:
                end_arr.append(item)
    for i in start_arr:
        if start_arr[i][0] < current_time < start_arr[i][1] and len(end_arr) % 2 == 0:
            return start_arr[i][1]
        elif len(end_arr) % 2 != 0:
            return end_arr[-1]
    return 'available'


def main():
    print(check_availability(["09:30-10:15", "12:20-15:50"], "10:00"))


if __name__ == "__main__":
    main()
