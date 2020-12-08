from dataclasses import dataclass

from typing import List


@dataclass
class PasswordRules:
    """Class for representing password rules"""
    min_count: int
    max_count: int
    letter: chr


def parse_password_rules(password_rule: str) -> PasswordRules:
    bounds, letter, _ = password_rule.split(" ")
    low, high = bounds.split("-")
    return PasswordRules(int(low), int(high), letter[0])


def validate_password(password_rule: PasswordRules, password: str) -> bool:
    count = password.count(password_rule.letter)
    return password_rule.min_count <= count <= password_rule.max_count


def part1(password_rules_list: List[str]) -> int:
    valid_passwords = 0
    for item in password_rules_list:
        rules = parse_password_rules(item)
        password = item.split()[2]
        valid_passwords += 1 if validate_password(rules, password) else 0
    return valid_passwords


if __name__ == "__main__":
    password_list = open("day2.txt").read().split("\n")
    print(part1(password_list))
