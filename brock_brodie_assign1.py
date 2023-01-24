print("===============================================================")
print("Shipping Calculator")
choice = 'y'
while(choice == 'y'):
    print("===============================================================")
    cost = float(input("Cost of items ordered: "))
    while(cost<0):
        print("You must enter a positive number. Please try again.")
        cost = float(input("Cost of items ordered: "))
    shipCost = 0
    if(cost < 30):
        shipCost = 5.95
    elif(cost<50):
        shipCost = 7.95
    elif(cost<75):
        shipCost = 9.95
    print("Shipping cost:            ",shipCost)
    print("Total cost:                %.2f"%(cost+shipCost))
    choice = input("Continue? (y/n): ")[0].lower()
print("===============================================================")
print("Bye!")