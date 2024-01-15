import csv
with open ('DSpro課題.csv')as csvfile:
    a = csv.reader(csvfile)
    for r in a:
        print(r)