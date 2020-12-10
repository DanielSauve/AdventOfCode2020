from typing import Set


def two_sum(preamble: Set[int], total: int) -> bool:
    for item in preamble:
        if total - item in preamble:
            return True
    return False


def part_1(raw_xmas: str) -> int:
    xmas_list = list(map(lambda x: int(x), raw_xmas.split()))
    for index, item in enumerate(xmas_list):
        if index < 25:
            continue
        preamble = set(xmas_list[index - 25:index])
        if not two_sum(preamble, item):
            return item
    return 0


if __name__ == "__main__":
    xmas = open("day9.txt").read()
    print(part_1(xmas))
