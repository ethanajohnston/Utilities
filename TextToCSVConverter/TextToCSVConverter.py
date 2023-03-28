import os
import csv

input_file = 'input.txt'
output_file = 'output.csv'

# Function to split the line into columns based on whitespace
def split_into_columns(line):
    columns = line.strip().split()
    return columns

# Change the working directory to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_writer = csv.writer(outfile)
    for line in infile:
        columns = split_into_columns(line)
        csv_writer.writerow(columns)

print(f"Processed {input_file} and saved the result to {output_file}.")
