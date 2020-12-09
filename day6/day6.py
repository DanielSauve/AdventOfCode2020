def part_1(questions: str) -> int:
    yes_count = 0
    for group in questions.split("\n\n"):
        yes_list = set()
        for person in group.split():
            yes_list = yes_list.union(set(list(person)))
        yes_count += len(yes_list)
    return yes_count


def part_2(questions: str) -> int:
    yes_count = 0
    for group in questions.split("\n\n"):
        yes_list = dict()
        for person in group.split():
            for answer in person:
                if answer in yes_list:
                    yes_list[answer] += 1
                else:
                    yes_list[answer] = 1
        for item, count in yes_list.items():
            if count == len(group.split()):
                yes_count += 1
    return yes_count


if __name__ == "__main__":
    all_questions = open("day6.txt").read()
    print(part_1(all_questions))
    print(part_2(all_questions))
