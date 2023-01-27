import json
import csv

with open('errors.json') as json_file:
    data = json.load(json_file)

csv_file = open('errors.csv', 'w')
csv_writer = csv.writer(csv_file)

for first_key in data.keys():
  for second_key in data[first_key].keys():
    string = data[first_key][second_key][0].upper()
    csv_writer.writerow([string])

csv_file.close()
