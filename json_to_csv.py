import json
import csv

with open('errors.json') as json_file:
    data = json.load(json_file)

csv_file = open('errors.csv', 'w')
csv_writer = csv.writer(csv_file)

for key in data.keys():
  for another_key in data[key].keys():
    csv_writer.writerow(data[key][another_key][0].upper())
csv_file.close()
