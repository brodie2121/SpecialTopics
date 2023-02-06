try:
    # Open the file for reading
    with open("file.txt", "r") as f:
        even_numbers = ""
        odd_numbers = "" 
        for line in f:
            number = int(line)
            if number % 2 == 0:
                even_numbers += str(number) + "\n"
            else:
                odd_numbers += str(number) + "\n"
except FileNotFoundError:
    print("File not found.")

try:
    # Open the file for writing even numbers
    with open("even_numbers.txt", "w") as f:
        f.write(even_numbers)
    # Open the file for writing odd numbers
    with open("odd_numbers.txt", "w") as f:
        f.write(odd_numbers)
except:
    print("Error opening/writing to file.")

f.close()