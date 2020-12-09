def part_1(questions: str) -> int:
    yes_count = 0
    for group in questions.split("\n\n"):
        yes_list = set()
        for person in group.split():
            yes_list = yes_list.union(set(list(person)))
        yes_count += len(yes_list)
    return yes_count


if __name__ == "__main__":
    all_questions = open("day6.txt").read()
    print(part_1(all_questions))
