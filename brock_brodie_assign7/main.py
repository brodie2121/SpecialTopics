from product import Product


def main():
    products = []
    choice = 'y'
    while choice.lower() == 'y':
        name = input("Enter a product name: ")
        price = float(input("Enter a price for this product: "))
        discount_percent = float(input("Enter a discount percentage: "))
        product = Product(name, price, discount_percent)
        products.append(product)
        choice = input("Enter another product? (Enter y/n): ")

    print("\nPRODUCTS:\n==================\n")
    for product in products:
        print(product)
        print()


if __name__ == '__main__':
    main()
