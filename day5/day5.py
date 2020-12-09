def find_row(code: str) -> int:
    low, high = 0, 127
    for item in code[:-1]:
        if item == "F":
            high = (low + high) // 2
        elif item == "B":
            low = round((low + high) / 2)
    return low if code[-1] == "F" else high


def find_column(code: str) -> int:
    low, high = 0, 7
    for item in code[:-1]:
        if item == "L":
            high = (low + high) // 2
        elif item == "R":
            low = round((low + high) / 2)
    return low if code[-1] == "L" else high


def part_1(batch_file: str) -> int:
    boarding_passes = batch_file.split()
    return max(
        map(lambda boarding_pass: find_row(boarding_pass[:-3]) * 8 + find_column(boarding_pass[-3:]), boarding_passes))


if __name__ == "__main__":
    boarding_input = open("day5.txt").read()
    print(part_1(boarding_input))
