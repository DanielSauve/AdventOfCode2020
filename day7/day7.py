from typing import Dict


def parse_contains(contains: str) -> Dict[str, int]:
    if contains == "no other bags.":
        return {}
    output = {}
    contains = contains[:-1]
    for item in contains.split(", "):
        bags_index = item.index(" bag")
        output[item[2:bags_index]] = int(item[0])
    return output


def can_contain(bag_map: Dict[str, Dict[str, int]], start_bag: str, end_bag: str, memo: Dict[str, bool]) -> bool:
    if start_bag in memo:
        return memo[start_bag]
    if end_bag in bag_map[start_bag]:
        memo[start_bag] = True
        return True
    for bag in bag_map[start_bag].keys():
        if can_contain(bag_map, bag, end_bag, memo):
            memo[start_bag] = True
            return True
    memo[start_bag] = False
    return False


def part_1(bag_rules: str) -> int:
    bag_rules_list = bag_rules.split("\n")
    bag_map: Dict[str, Dict[str, int]] = dict()
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


def count_bags_in(bag_map: Dict[str, Dict[str, int]], start_bag: str) -> int:
    sub_bags = bag_map[start_bag]
    if len(sub_bags) == 0:
        return 1
    bag_count = 1
    for bag, count in sub_bags.items():
        bag_count += count * count_bags_in(bag_map, bag)
    return bag_count


def part_2(bag_rules: str) -> int:
    bag_rules_list = bag_rules.split("\n")
    bag_map: Dict[str, Dict[str, int]] = dict()
    for rule in bag_rules_list:
        bag, contains = rule.split(" bags contain ")
        bag_map[bag] = parse_contains(contains)
    return count_bags_in(bag_map, "shiny gold") - 1


if __name__ == "__main__":
    raw_bag_rules = open("day7.txt").read()
    print(part_1(raw_bag_rules))
    print(part_2(raw_bag_rules))
