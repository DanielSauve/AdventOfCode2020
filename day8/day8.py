from typing import Set


def part_1(instructions: str) -> int:
    accumulator = 0
    instruction_pointer = 0
    instructions_seen: Set[int] = set()
    instruction_list = instructions.split("\n")
    while instruction_pointer not in instructions_seen:
        instructions_seen.add(instruction_pointer)
        opcode, operand = instruction_list[instruction_pointer].split()
        if opcode == "nop":
            instruction_pointer += 1
        elif opcode == "jmp":
            instruction_pointer += int(operand)
        elif opcode == "acc":
            accumulator += int(operand)
            instruction_pointer += 1
    return accumulator


if __name__ == "__main__":
    raw_instructions = open("day8.txt").read()
    print(part_1(raw_instructions))
