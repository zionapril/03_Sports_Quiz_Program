import csv

with open('03_Sports_Quiz_Program\\team_stadium.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)