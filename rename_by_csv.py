import csv
import os

with open("filename.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        try:
            os.rename(line[0], line[1])
        except FileNotFoundError:
            pass
