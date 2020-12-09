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


def compute_id(boarding_pass: str) -> int:
    return find_row(boarding_pass[:-3]) * 8 + find_column(boarding_pass[-3:])


def part_1(batch_file: str) -> int:
    boarding_passes = batch_file.split()
    return max(map(compute_id, boarding_passes))


def part_2(batch_file: str) -> int:
    boarding_passes = batch_file.split()
    seat_ids = sorted((map(compute_id, boarding_passes)))
    prev_id = seat_ids[0]
    for seat_id in seat_ids[1:]:
        if prev_id != seat_id - 1:
            return seat_id - 1
        prev_id = seat_id
    return -1


if __name__ == "__main__":
    boarding_input = open("day5.txt").read()
    print(part_1(boarding_input))
    print(part_2(boarding_input))
