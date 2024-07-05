import csv
import json

csv_file_list = ["establishment_stats_earth", "establishment_stats_interplanetary",
                 "revocation_table_earth", "revocation_table_interplanetary"]

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for key, value in row.items():
                try:
                    if "cmark" in value:
                        row[key] = True

                    row[key] = round(float(value), 3)

                except ValueError:
                    pass
            data.append(row)

    with open(json_file, "w") as json_file:
        json.dump(data, json_file, indent=4)

for csv_file in csv_file_list:
    csv_to_json(f"data/csv/{csv_file}.csv", f"data/json/{csv_file}.json")

