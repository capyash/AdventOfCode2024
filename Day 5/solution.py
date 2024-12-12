from collections import namedtuple
import pathlib
from typing import List

base_path = pathlib.Path(__file__).parent

sample_path = pathlib.Path.joinpath(base_path, "sample.txt")
data_path = pathlib.Path.joinpath(base_path, "data.txt")

source_path = sample_path
source_path = data_path  # Uncomment to use full data

input_data = []

print(pathlib.Path(__file__))

Order = namedtuple("Order", ["before", "after"])

with open(file=source_path) as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]
    # print(input_data)

ordering_data = [
    Order(int(y.split(sep="|")[0]), int(y.split(sep="|")[1]))
    for y in input_data
    if "|" in y
]
print_data = [x for x in input_data if "|" not in x and x != ""]

# print(ordering_data)
# print(print_data)

# Part 1

sum_mid_pages = 0
incorrect_updates: List[List[int]] = []


# Logic
# For each value in every line of print_data, we need to see if the values after the value are 'before' the value in the order array.
# For each value in every line of print_data, we need to see if the values before the value are 'after' the value in the order array.
def check_validity_and_return_bad_match(ordering_data: List[Order], pages: List[int]):
    bad_match_info = None
    for index, page in enumerate(pages):
        # For each value in every line of print_data,
        # we need to see if the values after the value are
        # 'before' the value in the order array.
        # If this value is not the last value, find all Order where it's the 'after' value
        if index != (len(pages) - 1):
            before_orders = [x for x in ordering_data if x.after == page]
            if len(before_orders):
                # If there are any such matches, first get the values after this value in the array.
                after_values = pages[index + 1 :]
                for after_index, after_value in enumerate(after_values):
                    for before_order in before_orders:
                        if after_value == before_order.before:
                            bad_match_info = (
                                index,
                                after_index + index + 1,
                                before_order,
                            )
                            return False, bad_match_info

        # For each value in every line of print_data,
        # we need to see if the values before the value are
        # 'after' the value in the order array.

        # If this value is not the first value find all Order where it's the 'after value
        if index != 0:
            after_orders = [x for x in ordering_data if x.before == page]
            if len(after_orders):
                # If there are any such matches, first get the values before this value in the array.
                before_values = pages[:index]
                for before_index, before_value in enumerate(before_values):
                    for after_order in after_orders:
                        if before_value == after_order.after:
                            bad_match_info = (index, before_index, after_order)
                            return False, bad_match_info
    return True, bad_match_info


for single_print in print_data:
    is_valid = True
    pages = [int(x) for x in single_print.split(",")]
    mid_page = pages[len(pages) // 2]
    (is_valid, bad_match_info) = check_validity_and_return_bad_match(
        ordering_data, pages
    )
    if is_valid:
        sum_mid_pages += mid_page
    else:
        incorrect_updates.append(pages)

print("Sum Mid Pages: ", sum_mid_pages)

# print("Incorrect", incorrect_updates)

sum_mid_pages = 0

for incorrect_update in incorrect_updates:
    # print("Fixing: ", incorrect_update)
    while True:
        (is_valid, bad_match_info) = check_validity_and_return_bad_match(
            ordering_data, incorrect_update
        )
        if is_valid:
            sum_mid_pages += incorrect_update[len(incorrect_update) // 2]
            break
        # print("Current: ", incorrect_update)
        # print("Is Valid? ", is_valid)
        # print("Bad match info:", bad_match_info)
        x, y = incorrect_update[bad_match_info[0]], incorrect_update[bad_match_info[1]]
        incorrect_update[bad_match_info[0]], incorrect_update[bad_match_info[1]] = y, x
        # print("New: ", incorrect_update)
        # break

    # break

print("Sum Fixed Mid Pages: ", sum_mid_pages)
