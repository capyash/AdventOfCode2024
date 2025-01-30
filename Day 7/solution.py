import pathlib
from typing import Deque, List
from collections import deque

from tqdm.auto import tqdm

base_path = pathlib.Path(__file__).parent

sample_path = pathlib.Path.joinpath(base_path, "sample2.txt")
data_path = pathlib.Path.joinpath(base_path, "data.txt")

source_path = sample_path
# source_path = data_path  # Uncomment to use full data

input_data = []

print(pathlib.Path(__file__))

with open(file=source_path) as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]
    # print(input_data)


def calculate(values: Deque[str]):
    # print(*values)
    if len(values) == 0:
        return 0
    if len(values) % 2 == 0:
        raise ValueError("Queue can't have uneven elements")
    total = int(values.popleft())
    while len(values):
        action = values.popleft()
        right = int(values.popleft())
        match action:
            case "+":
                total += right
            case "*":
                total *= right
            case _:
                raise ValueError(f"Unknown action: {action}")
    # print(f" = {total}")
    return total


def find_sums(target: int, numbers: List[str], cache={}) -> bool:

    deq_numbers = deque(numbers)
    current_sum = calculate(deq_numbers)
    if current_sum == target:
        return True
    if current_sum > target:
        return False
    # Find "+"s
    num_str = "".join(numbers)
    if num_str in cache:
        return cache[num_str]
    found = False
    plus_indices = [i for i, x in enumerate(numbers) if x == "+"]
    for index in plus_indices:
        # Replace each "+" with a "*"
        new_numbers = numbers.copy()
        new_numbers[index] = "*"
        if find_sums(target, new_numbers, cache):
            found = True
    cache[num_str] = found
    return found


valid_counter = 0
valid_sum = 0

for equation in tqdm(input_data):
    eq_sum = int(equation[: equation.index(":")])
    eq_values = []
    [
        eq_values.extend([x, "+"])
        for x in equation[equation.index(":") + 1 :].strip().split(" ")
    ]
    eq_values = eq_values[:-1]
    eq_plus = eq_values.copy()
    if calculate
    # print(f"equation:'{equation}', sum: {eq_sum}, eq_values: {eq_values}")
    if find_sums(eq_sum, eq_values):
        # print("Valid")
        valid_counter += 1
        valid_sum += eq_sum
    # else:
    #    print("Not Valid")

print(f"Valid Equations: {valid_counter} with sum: {valid_sum}")
