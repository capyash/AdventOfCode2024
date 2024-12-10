import pathlib
from typing import List
from collections import namedtuple

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
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]
    input_grid: List[List[str]] = []
    [input_grid.extend([list(line)]) for line in input_data]
    # print_grid(input_grid)


Coordinates = namedtuple("Coordinates", ["row", "column"])

xmas_counter = 0


def get_next_point(
    point: Coordinates, row_diff: int, col_diff: int, grid: List[List[str]]
):
    new_row = point.row + row_diff
    new_col = point.column + col_diff

    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
        return Coordinates(new_row, new_col)
    else:
        return None


# Part 1
# Find all 'X's, then find neighboring 'M's and follow along the line.
for row in range(len(input_grid)):  # i is row
    for col in range(len(input_grid[row])):  # j is column
        raw_neighbors = [
            Coordinates(row - 1, col - 1),  # Top Left
            Coordinates(row - 1, col),  # Top
            Coordinates(row - 1, col + 1),  # Top Right
            Coordinates(row, col - 1),  # Left
            Coordinates(row, col + 1),  # Right
            Coordinates(row + 1, col - 1),  # Bottom Left
            Coordinates(row + 1, col),  # Bottom
            Coordinates(row + 1, col + 1),  # Bottom Right
        ]
        valid_neighbors = [
            point
            for point in raw_neighbors
            if 0 <= point.row < len(input_grid)
            and 0 <= point.column < len(input_grid[row])
        ]

        if input_grid[row][col] == "X":
            for point in valid_neighbors:
                if input_grid[point.row][point.column] == "M":
                    row_diff = point.row - row
                    col_diff = point.column - col
                    opposite_point = get_next_point(
                        point, row_diff, col_diff, input_grid
                    )
                    if (
                        opposite_point is not None
                        and input_grid[opposite_point.row][opposite_point.column] == "A"
                    ):
                        opposite_point = get_next_point(
                            opposite_point, row_diff, col_diff, input_grid
                        )
                        if (
                            opposite_point is not None
                            and input_grid[opposite_point.row][opposite_point.column]
                            == "S"
                        ):
                            xmas_counter += 1

print(f"XMAS Count: {xmas_counter}")

# print_grid(input_grid)
# Part 2
x_mas_counter = 0
# Find all 'A's, then Find 'M's and opposing 'S's
for row in range(len(input_grid)):  # i is row
    for col in range(len(input_grid[row])):  # j is column
        raw_neighbors = [
            Coordinates(row - 1, col - 1),  # Top Left
            # Coordinates(row - 1, col),  # Top
            Coordinates(row - 1, col + 1),  # Top Right
            # Coordinates(row, col - 1),  # Left
            # Coordinates(row, col + 1),  # Right
            Coordinates(row + 1, col - 1),  # Bottom Left
            # Coordinates(row + 1, col),  # Bottom
            Coordinates(row + 1, col + 1),  # Bottom Right
        ]
        valid_neighbors = [
            point
            for point in raw_neighbors
            if 0 <= point.row < len(input_grid)
            and 0 <= point.column < len(input_grid[row])
        ]

        if input_grid[row][col] == "A":
            is_x_mas = False
            for point in valid_neighbors:
                if input_grid[point.row][point.column] == "M":
                    row_diff = point.row - row
                    col_diff = point.column - col
                    opposite_point = get_next_point(
                        Coordinates(row, col), -row_diff, -col_diff, input_grid
                    )
                    if (
                        opposite_point is not None
                        and input_grid[opposite_point.row][opposite_point.column] == "S"
                    ):
                        side_points = [
                            get_next_point(
                                Coordinates(row, col), -row_diff, col_diff, input_grid
                            ),
                            get_next_point(
                                Coordinates(row, col), row_diff, -col_diff, input_grid
                            ),
                        ]
                        if (
                            None not in side_points
                            and "M"
                            in [
                                input_grid[side_point.row][side_point.column]
                                for side_point in side_points
                            ]
                            and "S"
                            in [
                                input_grid[side_point.row][side_point.column]
                                for side_point in side_points
                            ]
                        ):
                            is_x_mas = True

            if is_x_mas:
                x_mas_counter += 1
print(f"X-MAS Count: {x_mas_counter}")
