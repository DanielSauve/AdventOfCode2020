from typing import List


def parse_trees(trees: str) -> List[str]:
    return trees.split("\n")


def part_1(trees: str) -> int:
    tree_grid = parse_trees(trees)
    current_x = 3
    trees_encountered = 0
    for current_y in range(1, len(tree_grid)):
        if tree_grid[current_y][current_x] == "#":
            trees_encountered += 1
        current_x = (current_x + 3) % len(tree_grid[current_y])
        pass
    return trees_encountered


if __name__ == "__main__":
    trees_input = open("day3.txt").read()
    print(part_1(trees_input))
