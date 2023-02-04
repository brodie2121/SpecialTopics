import conversion

def main():
  print(conversion.displayMenu())

  while True:
    choice = input("Enter your conversion choice (a or b): ")

    if choice == "a":
      feet = float(input("Enter number of feet: "))
      result = conversion.feetToMeters(feet)
    elif choice == "b":
      meters = float(input("Enter number of meters: "))
      result = conversion.metersToFeet(meters)
    else:
      print("Invalid choice, please try again.")
      continue

    print("Result:", round(result, 2))

    again = input("Do you want to continue? (y/n) ")
    if again == "n":
      break

  print("Bye!")

if __name__ == "__main__":
  main()