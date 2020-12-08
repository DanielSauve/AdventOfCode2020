def two_sum(numbers: set, total: int):
    for number in numbers:
        if 2020 - number in numbers:
            return number * (2020 - number)


def three_sum(numbers: set, total: int):
    for first in numbers:
        for second in numbers:
            if second == first:
                continue
            if 2020 - first - second in numbers:
                return first * second * (2020 - first - second)


if __name__ == "__main__":
    numbers = set(int(i) for i in open("day1.txt").read().split())
    print(two_sum(numbers, 2020))
    print(three_sum(numbers, 2020))
