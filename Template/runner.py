file_path1 = "sample.txt"
file_path2 = "data.txt"


input_data = []

with open(file=file_path2) as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]
