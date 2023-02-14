def display_header():
    print("The Quarterly Sales program")

def get_quarterly_sales():
    sales = []
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    for quarter in quarters:
        sales.append(float(input(f"Enter sales for {quarter}: ")))
    return sales

def process_sales(sales):
    total = sum(sales)
    average = total / len(sales)
    minimum = min(sales)
    maximum = max(sales)
    print("Total: $%.2f" % total)
    print("Average Quarter: $%.2f" % average)
    print("Lowest Quarter: $%.2f" % minimum)
    print("Highest Quarter: $%.2f" % maximum)

def main():
    display_header()
    sales = get_quarterly_sales()
    process_sales(sales)

if __name__ == "__main__":
    main()
