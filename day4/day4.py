import re


def passport_has_valid_fields(passport: str) -> bool:
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in expected_fields:
        if field not in passport:
            return False
    return True


def part_1(batch_file: str) -> int:
    valid_passports = 0
    passport_list = batch_file.split("\n\n")
    for passport in passport_list:
        valid_passports += 1 if passport_has_valid_fields(passport) else 0
    return valid_passports


field_validation = {
    "byr": lambda birth_year: 1920 <= int(birth_year) <= 2002,
    "iyr": lambda issue_year: 2010 <= int(issue_year) <= 2020,
    "eyr": lambda expiry_year: 2020 <= int(expiry_year) <= 2030,
    "hgt": lambda height: (re.match(r"[\d]+cm", height) and 150 <= int(re.match(r"[\d]+", height).group()) <= 193) or (
            re.match(r"[\d]+in", height) and 59 <= int(re.match(r"[\d]+", height).group()) <= 76),
    "hcl": lambda hair_colour: re.match(r"#[\da-f]{6}", hair_colour),
    "ecl": lambda eye_colour: eye_colour in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda passport_id: re.match(r"^[\d]{9}$", passport_id),
    "cid": lambda country_id: True
}


def part_2(batch_file: str) -> int:
    valid_passports = 0
    passport_list = batch_file.split("\n\n")
    for passport in passport_list:
        valid = passport_has_valid_fields(passport)
        fields = passport.split()
        for field in fields:
            field_name, field_value = field.split(":")
            if not field_validation[field_name](field_value):
                valid = False
        valid_passports += 1 if valid else 0
    return valid_passports


if __name__ == "__main__":
    batch_input = open("day4.txt").read()
    print(part_1(batch_input))
    print(part_2(batch_input))
