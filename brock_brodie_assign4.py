import csv

def read_data(filename = "nutrition_data.csv"): #default filename
    """
    This function reads the csv file and returns a list of lists.
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f) 
        data = list(reader)
    return data

def create_separate_list(main_list, user_choice):
    """
    This function creates a list of lists based on the user's choice.
    """
    food_group_list = []   
    if user_choice == 1:    
        choice = "Dairy"    
    elif user_choice == 2:  
        choice = "Meat"     
    elif user_choice == 3: 
        choice = "Vegetables"   
    elif user_choice == 4:  
        choice = "Fruit"    
    elif user_choice == 5:  
        choice = "Grains"   
    else:
        print("Invalid choice")  
    for row in main_list: 
        if row[0] == choice:  
            food_group_list.append(row)  
    return food_group_list 

def display_menu():
    """
    This function prints the menu to the screen.
    """
    print("Nutrition by Food Group")
    print("1. Dairy")
    print("2. Meat")
    print("3. Vegetables")
    print("4. Fruit")
    print("5. Grains")
    print("Enter your food group choice: (1-5): ")

def main():
    """
    This function contains the code loop for user interaction.
    """
    main_list = read_data()  
    while True: 
        display_menu()  
        user_choice = int(input())  
        if user_choice < 1 or user_choice > 5: 
            print("Warning: Please enter a number between 1 and 5")  
        else:     # if the user's choice is 1-5
            food_group_list = create_separate_list(main_list, user_choice)  
            print("{:<20}{:<20}{:<20}".format("Name", "Amount", "Calories"))      
            for row in food_group_list: 
                print("{:<20}{:<20}{:<20}".format(row[1], row[2], row[3])) 
            print("Would you like to perform another conversion? (y/n): ") 
            user_choice = input()     
            if user_choice == "n":
                break    

main()