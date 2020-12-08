from typing import List
from functools import reduce


def parse_trees(trees: str) -> List[str]:
    return trees.split("\n")


def traverse_trees(tree_grid: List[str], x_increment: int, y_increment: int) -> int:
    trees_encountered = 0
    current_x = x_increment
    current_y = y_increment
    tree_grid_width = len(tree_grid[0])
    while current_y < len(tree_grid):
        if tree_grid[current_y][current_x] == "#":
            trees_encountered += 1
        current_x = (current_x + x_increment) % tree_grid_width
        current_y += y_increment
    return trees_encountered


def part_1(trees: str) -> int:
    tree_grid = parse_trees(trees)
    return traverse_trees(tree_grid, 3, 1)


def part_2(trees: str) -> int:
    tree_grid = parse_trees(trees)
    return reduce(lambda x, y: x * y, [traverse_trees(tree_grid, i, 1) for i in [1, 3, 5, 7]]) * traverse_trees(
        tree_grid, 1, 2)


if __name__ == "__main__":
    trees_input = open("day3.txt").read()
    print(part_1(trees_input))
    print(part_2(trees_input))
