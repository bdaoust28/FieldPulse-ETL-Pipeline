import csv, openpyxl

# STEP 2: append price to each row
class dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

def swap():
    items = csv.reader(open('items-stripped.csv', newline='', encoding='utf8'), delimiter=',')
    codes = csv.DictReader(open('codes.csv', newline='', encoding='utf8'), delimiter=',')
    codes_dict = dictionary()

    # add code matrix to dictionary
    counter = 1
    for row in codes:
        codes_dict.add(counter, row)
        counter += 1

    # append price to each row by looking up code in dict
    with open('swap.csv', 'w+', newline='') as swap:
        writer = csv.writer(swap, delimiter=',')
        iteritems = iter(items)
        next(iteritems)
        for item_row in items:
            code = item_row[3][0]                   # get letter
            num = int(item_row[3][1:])              # get number
            item_row.append(codes_dict[num][code])  # lookup letter + number in dict and append
            writer.writerow(item_row)               # write to 'swap.csv'

if __name__ == '__main__':
    swap()