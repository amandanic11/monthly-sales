# reporter.py

import os
import operator
import pandas as pd

      
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

csv_filename = "monthly_sales.csv"
csv_filepath = os.path.join("data", csv_filename)

sales = pd.read_csv(csv_filepath)
#print(sales.head)
total_sales = sales["sales price"].sum()
#print(total_sales)

month = "MARCH"
year = 2017

print("SALES REPORT")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")



# print(sales)

# print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2017...")

# print("SALES REPORT (OCTOBER 2017)")
# print("TOTAL SALES:", to_usd(sales["sales price"].sum())
#print("TOP SELLING PRODUCTS")
