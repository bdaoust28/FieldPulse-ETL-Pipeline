# Written by Beau Daoust (2022)
import strip, price_swap, input_data

# runs all modules
def main():
    strip.strip()       # strips all whitespace from list
    price_swap.swap()   # appends price to every item
    input_data.input()  # processes and outputs all data to xlsx

if __name__ == '__main__':
    main()