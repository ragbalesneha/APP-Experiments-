import csv
import json

input_file = r"C:\Users\Admin\Downloads\students.csv"
output_file = "students.json"

with open(input_file, "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV file '{input_file}' converted to JSON file '{output_file}' successfully!")
print("JSON file created:", output_file)