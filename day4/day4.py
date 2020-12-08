def part_1(batch_file: str) -> int:
    valid_passports = 0
    passport_list = batch_file.split("\n\n")
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passport_list:
        valid = True
        for field in expected_fields:
            if field not in passport:
                valid = False
                break
        valid_passports += 1 if valid else 0
    return valid_passports


if __name__ == "__main__":
    batch_input = open("day4.txt").read()
    print(part_1(batch_input))
