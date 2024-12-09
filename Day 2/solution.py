import pathlib, math
from typing import List

base_path = pathlib.Path(__file__).parent

sample_path = pathlib.Path.joinpath(base_path, "sample.txt")
data_path = pathlib.Path.joinpath(base_path, "data.txt")

source_path = sample_path
source_path = data_path  # Uncomment to use full data

input_data = []

# print(pathlib.Path(__file__))

with open(file=source_path) as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]
    # print(input_data)


def remove_level_and_recheck(original_report_levels: List[int], new_tolerance: int):
    return any(
        is_report_safe(
            original_report_levels[:i] + original_report_levels[i + 1 :], new_tolerance
        )
        for i in range(len(original_report_levels))
    )


def is_report_safe(report_levels: List[int], tolerance=0):
    # print(report_levels)
    trend = 0
    is_safe = True
    for i in range(1, len(report_levels)):
        # First, get diff between current and previous
        diff = report_levels[i] - report_levels[i - 1]

        # If diff is less than one or greater than three, not safe
        if abs(diff) < 1 or abs(diff) > 3:
            # print(
            #     f"Difference between {report_levels[i-1]} and {report_levels[i]} out of range: {abs(diff)}."
            # )
            if tolerance > 0:
                is_safe = remove_level_and_recheck(report_levels, tolerance - 1)
            else:
                is_safe = False
            break

        if not is_safe:
            break

        # If diff is not same +ve/-ve trend, not safe
        if trend == 0:
            trend = diff // abs(diff)  # Set to +1 or -1
        else:
            # see if trend continues
            new_trend = diff // abs(diff)
            if new_trend != trend:
                # print(
                #     f"Previous trend was {trend} but between {report_levels[i - 1]} and {report_levels[i]} is {new_trend}."
                # )
                if tolerance > 0:
                    is_safe = remove_level_and_recheck(report_levels, tolerance - 1)
                else:
                    is_safe = False
                break

        if not is_safe:
            break
    # print("Is this safe? ", is_safe)
    return is_safe


# Part 1
part_1_safe_count = 0

for report in input_data:

    # print("\n--------------\n")

    # Convert to list of ints
    report_levels = list(int(value) for value in report.split(" "))

    # print(report_levels)
    is_safe = is_report_safe(report_levels, tolerance=0)

    # print(report_levels, is_safe)

    # Mark as safe
    if is_safe:
        part_1_safe_count += 1

print("Part 1 Safe: ", part_1_safe_count)

# Part 2
part_2_safe_count = 0

for report in input_data:

    # print("\n--------------\n")

    # Convert to list of ints
    report_levels = list(int(value) for value in report.split(" "))

    # print(report_levels)
    is_safe = is_report_safe(report_levels, tolerance=1)

    # print(report_levels, is_safe)

    # Mark as safe
    if is_safe:
        part_2_safe_count += 1

print("Part 2 Safe: ", part_2_safe_count)
