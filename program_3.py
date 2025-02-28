#By: Sabria Fafach
#Date: Febuary 28, 2025
#Name: program_3.py

STATE_SALES_TAX_RATE=0.05
COUNTY_SALES_TAX_RATE=0.025
TOTAL_MONTHLY_SALES=float(input("Enter the total monthly sales in dollars:"))

def calculate_county_sales_tax():
    return COUNTY_SALES_TAX_RATE*TOTAL_MONTHLY_SALES

def calculate_state_sales_tax():
    return STATE_SALES_TAX_RATE*TOTAL_MONTHLY_SALES

def main():

    state_sales_tax=calculate_state_sales_tax()
    print(f"The amount of state sales tax for this month is ${state_sales_tax:.2f}.")

    county_sales_tax=calculate_county_sales_tax()
    print(f"The amount of state sales tax for this month is ${county_sales_tax:.2f}.")

    total_tax=state_sales_tax+county_sales_tax
    print(f"The total tax for this month is ${total_tax:.2f}.")

main()