import csv
rows = csv.reader(open("file.csv", "rb"))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open("file.csv", "wb"))
writer.writerows(newrows)
