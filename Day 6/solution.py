from enum import Enum
import pathlib
from typing import List, Literal, Tuple
from copy import deepcopy

from tqdm.auto import tqdm

base_path = pathlib.Path(__file__).parent

sample_path = pathlib.Path.joinpath(base_path, "sample.txt")
data_path = pathlib.Path.joinpath(base_path, "data.txt")

source_path = sample_path
source_path = data_path  # Uncomment to use full data

input_data = []

print(pathlib.Path(__file__))


def print_grid(grid: List[List[str]]):
    print("---------")
    print(" ", *list(range(len(grid))))
    [print(index, *line) for index, line in enumerate(grid)]
    print("---------")


with open(file=source_path) as f:
    while line := f.readline():
        input_data.append([x.strip() for x in line if x.strip() is not ""])
    # print(input_data)

# print_grid(input_data)


def find_char(grid: List[List[str]], char: str):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == char:
                return (row, col)
    return None


class Facing(Enum):
    N = (-1, 0)
    S = (1, 0)
    E = (0, 1)
    W = (0, -1)

    def turn_right(self):
        return {
            Facing.N: Facing.E,
            Facing.E: Facing.S,
            Facing.S: Facing.W,
            Facing.W: Facing.N,
        }.get(self)


initial_guard_position = find_char(input_data, "^")
initial_guard_facing = Facing.N

# print(guard_position)


def is_in_bounds(grid: List[List[str]], position: Tuple[int, int]):
    row, column = position[0], position[1]
    return 0 <= row < len(grid) and 0 <= column < len(grid[row])


def take_action(grid: List[List[str]], position: Tuple[int, int], facing: Facing):
    next_pos = (position[0] + facing.value[0], position[1] + facing.value[1])
    if not is_in_bounds(grid, next_pos):
        return (None, None, None)
    if grid[next_pos[0]][next_pos[1]] == "#":
        return (0, position, facing.turn_right())
    else:
        return (1, next_pos, facing)


# take_action(input_data, guard_position, Facing.N)

# Part 1

visited = set()

guard_position = initial_guard_position
guard_facing = initial_guard_facing
while is_in_bounds(input_data, guard_position):
    visited.add(guard_position)
    _, guard_position, guard_facing = take_action(
        input_data, guard_position, guard_facing
    )
    if _ is None:
        break

print("Distinct", len(visited))

# Part 2

potential_loop_counter = 0

for row, column in tqdm(visited):

    if input_data[row][column] != ".":
        continue
    new_grid = deepcopy(input_data)
    new_grid[row][column] = "#"
    guard_position = initial_guard_position
    guard_facing = initial_guard_facing
    facing_visited = set()
    # print_grid(new_grid)
    # break
    # print(guard_facing, guard_position)
    while is_in_bounds(new_grid, guard_position):
        if (guard_facing, guard_position) in facing_visited:
            potential_loop_counter += 1
            break

        facing_visited.add((guard_facing, guard_position))

        _, guard_position, guard_facing = take_action(
            new_grid, guard_position, guard_facing
        )
        if _ is None:
            break


print("Potential Loops", potential_loop_counter)
