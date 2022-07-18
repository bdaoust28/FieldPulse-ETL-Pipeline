# Invoice Item Import Spreadsheet Generator for FieldPulse
###### by Beau Daoust (2022)
This project an ETL pipeline which processes user-generated CSV data and loads it to a template XLSX file, ready to be uploaded (via the Mass Import functionality) to FieldPulse.

*DISCLAIMER: this project was specially written for an appliance-focused company, but can (and should) be modified to suit your needs. FieldPulse [does not recommend](https://help.fieldpulse.com/en/articles/2679548-importing-invoice-items) including special characters in the item name.*

**Project dependencies:**
   - openpyxl

Refer to **invoice_item_template.xlsx** to see a sample of the result.

### There are three CSV files the user must provide themselves:
1. **items.csv**
    * This contains all job data in the format of either: `Appliance,Type,Job,Code` or `Appliance,Type,Job,Code,Price`. 
    * Example: `Refrigerators & Freezers,Controls,Damper Control,A2,60.00`
2. **codes.csv**
    * This contains a matrix of prices to associate with each job. 
    * Example:
        ```
        CODES,A,B,C
        1,50.00,60.00,70.00
        2,60.00,70.00,80.00
        ```
    * Only necessary if prices aren't already included in **items.csv**. 
    If they are, exclude `price_swap.swap()` from ***master.py*** and modify ***input_data.py*** by replacing `'swap.csv'` with `'items_stripped.csv'`.
3. **sku.csv**
    * This contains data linking `Appliance` with 4-letter abbreviations for SKU generation. 
    * Example: ` Refrigerators & Freezers,REFR`

Once all CSV files and necessary modifications are made, run ***master.py*** to process data into a new file called **fieldpulse-upload.xlsx**.
Open it to verify results, then upload to FieldPulse when ready.


