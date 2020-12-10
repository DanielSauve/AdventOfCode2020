from copy import deepcopy
from typing import Set, List


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


def run_through(instruction_list: List[str]) -> int:
    accumulator = 0
    instruction_pointer = 0
    instructions_seen: Set[int] = set()
    while instruction_pointer < len(instruction_list):
        if instruction_pointer in instructions_seen:
            return -1
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


def part_2(instructions: str) -> int:
    instruction_list = instructions.split("\n")
    for index, item in enumerate(instruction_list):
        instruction_copy = deepcopy(instruction_list)
        if "acc" in item:
            continue
        if "nop" in item:
            instruction_copy[index] = instruction_copy[index].replace("nop", "jmp")
        elif "jmp" in item:
            instruction_copy[index] = instruction_copy[index].replace("jmp", "nop")
        acc = run_through(instruction_copy)
        if acc != -1:
            return acc
    return -1


if __name__ == "__main__":
    raw_instructions = open("day8.txt").read()
    print(part_1(raw_instructions))
    print(part_2(raw_instructions))
