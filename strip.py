# Written by Beau Daoust (2022)
import csv

# Step 1: strip all items of trailing whitespace
def strip():
    items = csv.reader(open('items.csv', newline='', encoding='utf8'), delimiter=',')
    with open('items-stripped.csv', 'w+', newline='') as s_items:
        writer = csv.writer(s_items, delimiter=',')
        for row in items:                   # row traversal
            for i in range(len(row)):       # item traversal
                row[i] = row[i].strip()     # strip whitespace
            writer.writerow(row)            # write new row to 'items_stripped.csv'

if __name__ == '__main__':
    strip()
