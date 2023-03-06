class Product:
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def discountAmount(self):
        return self.price * self.discountPercent / 100

    def discountedPrice(self):
        return self.price - self.discountAmount()

    def __str__(self):
        return 'Name: {}, Price: {}, Discount Percentage: {}%'.format(self.name, self.price, self.discountPercent)


def main():
    p1 = Product("Earphones", 1000, 10)
    p2 = Product("Art Resin", 525, 5)
    print(p1)
    print("Discount:", p1.discountAmount())
    print("Discounted Price:", p1.discountedPrice())
    print(p2)
    print("Discount:", p2.discountAmount())
    print("Discounted Price:", p2.discountedPrice())


main()
