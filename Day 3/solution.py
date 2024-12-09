import pathlib
import re
from typing import List

base_path = pathlib.Path(__file__).parent

sample_path = pathlib.Path.joinpath(base_path, "sample.txt")
data_path = pathlib.Path.joinpath(base_path, "data.txt")

source_path = sample_path
source_path = data_path  # Uncomment to use full data

input_data = []


with open(file=source_path) as f:
    input_data = f.read()
    # input_data = [x.strip() for x in input_data]

mul_regex = r"mul\(\d{1,3},\d{1,3}\)"

# Part 1
matches: List[str] = re.findall(mul_regex, input_data)

mul_sum = 0

for match in matches:
    clean_str = match[4:-1]
    values = list(int(x) for x in clean_str.split(","))
    mul_sum += values[0] * values[1]

print("Simple Sum:", mul_sum)

# Part 2

match_strings = []
remaining_input = input_data
# First Match
do_str = "do()"
dont_str = "don't()"
first_dont_index = remaining_input.index(dont_str)
match_strings.append(remaining_input[:first_dont_index])
remaining_input = remaining_input[first_dont_index + len(dont_str) :]
# print(match_strings)
# print(remaining_input)
include_in_total = False
while True:
    # Terminate when non string left
    if len(remaining_input) == 0:
        break

    # Currently in "don't" section
    if not include_in_total:
        try:
            next_do_index = remaining_input.index(do_str)
            remaining_input = remaining_input[next_do_index + len(do_str) :]
        except ValueError:
            # No more "do" sections, so we can stop processing.
            remaining_input = ""
            break
        include_in_total = True
        continue

    # Currently in "do" section
    if include_in_total:
        try:
            next_dont_index = remaining_input.index(dont_str)
        except ValueError:
            # No more don't sections, so include all remaining input
            match_strings.append(remaining_input)
            remaining_input = ""
            break
        match_strings.append(remaining_input[:next_dont_index])
        remaining_input = remaining_input[next_dont_index + len(dont_str) :]
        include_in_total = False
        continue

# print(match_strings)
# print(remaining_input)

matches = []
mul_sum = 0
[
    [
        matches.append(single_match)
        for single_match in re.findall(mul_regex, match_string)
    ]
    for match_string in match_strings
]
# print(matches)
for match in matches:
    clean_str = match[4:-1]
    values = list(int(x) for x in clean_str.split(","))
    mul_sum += values[0] * values[1]

print("Do/Don't Sum:", mul_sum)
