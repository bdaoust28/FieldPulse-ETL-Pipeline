# Written by Beau Daoust (2022)
import csv

# Step 1: strip all items of trailing whitespace
def strip():
    joblist = csv.reader(open('items.csv', newline='', encoding='utf8'), delimiter=',')
    with open('items-stripped.csv', 'w+', newline='') as s_items:
        writer = csv.writer(s_items, delimiter=',')
        for row in joblist:                 # row traversal
            for i, item in enumerate(row):  # item traversal
                row[i] = item.strip()       # strip whitespace
            writer.writerow(row)            # write new row to 'items_stripped.csv'

if __name__ == '__main__':
    strip()
