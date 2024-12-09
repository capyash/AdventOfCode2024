import pathlib

base_path  = pathlib.Path(__file__).parent

sample_path = pathlib.Path.joinpath(base_path,"sample.txt")
data_path = pathlib.Path.joinpath(base_path,"data.txt")

source_path = sample_path
# source_path = data_path # Uncomment to use full data

input_data = []

print(pathlib.Path(__file__))

with open(file=source_path) as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]
    print(input_data)

