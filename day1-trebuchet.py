def check_written(line, func):
    if func(line, 'one'):
        return 1
    if func(line, 'two'):
        return 2
    if func(line, 'three'):
        return 3
    if func(line, 'four'):
        return 4
    if func(line, 'five'):
        return 5
    if func(line, 'six'):
        return 6
    if func(line, 'seven'):
        return 7
    if func(line, 'eight'):
        return 8
    if func(line, 'nine'):
        return 9
    return -1


def get_number(line):
    first_number = -1
    last_number = -1
    n = len(line)
    i = 0
    while i < n and (first_number == -1 or last_number == -1):
        if first_number == -1 and line[i].isdigit():
            first_number = int(line[i])
        elif first_number == -1:
            first_number = check_written(line[i:], str.startswith)
        if last_number == -1 and line[- i - 1].isdigit():
            last_number = int(line[- i - 1])
        elif last_number == -1:
            last_number = check_written(line[:n - i], str.endswith)
        i += 1
    if first_number == -1:
        return 0
    return first_number * 10 + last_number


def trebuchet():
    summ = 0
    while True:
        try:
            summ += get_number(input())
        except EOFError:
            return summ


if __name__ == '__main__':
    print(trebuchet())
