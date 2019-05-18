from collections import defaultdict
import csv
import random

color_itr = 0
list_c = ["800000", "e6194b", "f58231", "ffe119", "bcf60c",\
     "3cb44b", "46f0f0", "4363d8", "911eb4", "f032e6", "808080", "9a6324", "808000", "008080", "000075", "000000", "fabebe"]

def genColor():
    global color_itr
    color = list_c[color_itr]
    color_itr += 1
    return color
    

csv_rows = []
with open('Hospitals.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    title = reader.fieldnames
    h_color_dict = {}
    for row in reader:
        h_type = row[title[4]]
        if h_type not in h_color_dict:
            h_color_dict[h_type] = genColor()
        row[title[5]] = h_color_dict[h_type]
        csv_rows.append(row)


with open('processed_hospitals_clean.csv', mode='w', newline='') as csv_file:
    fieldnames = title
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv_rows:
        writer.writerow(row)
