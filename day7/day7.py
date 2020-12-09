from typing import List, Dict


def parse_contains(contains: str) -> List[str]:
    if contains == "no other bags.":
        return []
    output = []
    contains = contains[:-1]
    for item in contains.split(", "):
        bags_index = item.index(" bag")
        output.append(item[2:bags_index])
    return output


def can_contain(bag_map: Dict[str, List[str]], start_bag: str, end_bag: str, memo: Dict[str, bool]) -> bool:
    if start_bag in memo:
        return memo[start_bag]
    if end_bag in bag_map[start_bag]:
        memo[start_bag] = True
        return True
    for bag in bag_map[start_bag]:
        if can_contain(bag_map, bag, end_bag, memo):
            memo[start_bag] = True
            return True
    memo[start_bag] = False
    return False


def part_1(bag_rules: str) -> int:
    bag_rules_list = bag_rules.split("\n")
    bag_map: Dict[str, List[str]] = dict()
    for rule in bag_rules_list:
        bag, contains = rule.split(" bags contain ")
        bag_map[bag] = parse_contains(contains)
    memo = dict()
    for bag in bag_map.keys():
        can_contain(bag_map, bag, "shiny gold", memo)
    bag_count = 0
    for item in memo.values():
        bag_count += 1 if item else 0
    return bag_count


if __name__ == "__main__":
    raw_bag_rules = open("day7.txt").read()
    print(part_1(raw_bag_rules))
