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


def part_2(raw_xmas: str, invalid_number: int) -> int:
    xmas_list = list(map(lambda x: int(x), raw_xmas.split()))
    for i in range(len(xmas_list)):
        for j in range(i + 1, len(xmas_list)):
            if sum(xmas_list[i:j]) == invalid_number:
                return min(xmas_list[i:j+1]) + max(xmas_list[i:j+1])
    return -1


if __name__ == "__main__":
    xmas = open("day9.txt").read()
    vulnerable = part_1(xmas)
    print(vulnerable)
    print(part_2(xmas, vulnerable))
