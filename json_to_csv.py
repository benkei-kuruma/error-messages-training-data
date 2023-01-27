import json
import csv

with open('errors.json') as json_file:
    data = json.load(json_file)

csv_file = open('errors.csv', 'w')
csv_writer = csv.writer(csv_file)

my_data = []
for key in data.keys():
    for value in data[key].values():
        csv_writer.writerow(value)
csv_file.close()
