from collections import defaultdict
import csv
import requests
import json

api_key = '1H732I32LI3V2LIJ3-VLI2U3VN2I3VU3R1-YR91279F91FY91F-Y81FH718OH13F81HF1F'
url = 'https://maps.googleapis.com/maps/api/geocode/json?'
csv_rows = []
with open('processed_hospitals.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    title = reader.fieldnames
    h_color_dict = {}
    for row in reader:
        h_lat = row[title[1]]
        if h_lat == "":
            h_name = row[title[3]]
            res_ob = requests.get(url + 'address =' +
                h_name + " New York" + '&key =' + api_key)
            geo_data = res_ob.json()
            row[title[1]] = geo_data['lat']
            row[title[2]] = geo_data['lng']
        csv_rows.append(row)
            


with open('processed_hospitals.csv', mode='w', newline='') as csv_file:
    fieldnames = title
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv_rows:
        writer.writerow(row)