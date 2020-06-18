import csv

# on Python 3.x use: open("input.csv", "r")  
with open("test.csv", "rb") as f_in:  # open input.csv for reading
    r = csv.reader(f_in)  # create a CSV reader
    header = next(r)  # store the header to recreate in the output
    columns_num = len(header)  # max number of columns
    # read in rows and fill potentially missing elements with 0 to ensure a perfect 2D list
    rows = []  # a storage for our rows
    for row in r:  # go through each CSV row
        columns = []  # a storage for our columns
        for index in range(columns_num):  # loop through each column index
            try:
                columns.append(int(row[index]))  # convert to integer and store in `columns`
            except (IndexError, ValueError, TypeError):  # invalid column value
                columns.append(0)  # store 0 to `columns` as an 'empty' value
        rows.append(columns)  # store the processed columns to the `rows`  storage

total_rows = float(len(rows))  # a number to take into the account for average
rows = zip(*rows)  # flip the CSV columns and rows, on Python 3.x use: list(zip(*rows))
for i, row in enumerate(rows):
    average_real = sum(row) / total_rows  # calculate the real average
    average = int(average_real)  # integer average, use as an average for non-floats
    if average_real - average != 0:  # the average is not an integer
        average = int(average_real * 100) / 100.0  # shorten the float to 2 decimals
    rows[i] = [column or average for column in row]  # apply to empty fields and update

# on Python 3.x use: with open("output.csv", "w", newline='')
with open("output.csv", "wb") as f_out:  # open output.csv for writing
    writer = csv.writer(f_out)
    writer.writerow(header)  # write the header to output CSV
    writer.writerows(zip(*rows))  # flip back rows and colums and write them to output CSV
