def display_menu():
    print("\nContacts Manager\n")
    print("view - View Contacts")
    print("add - Add Contact")
    print("del - Delete Contact")
    print("exit - Quit")

def view_contacts():
    with open("contacts.txt", "r") as file:
        print(file.read())

def add_contact(name, email, number):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{email},{number}\n")

def delete_contact(name):
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    with open("contacts.txt", "w") as file:
        for line in lines:
            if name not in line:
                file.write(line)

def main():
    display_menu()
    choice = (input("Enter choice: "))
    if choice == "view":
        view_contacts()
    elif choice == "add":
        name = input("Enter name: ")
        email = input("Enter email: ")
        number = input("Enter number: ")
        add_contact(name, email, number)
    elif choice == "del":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "exit":
        quit()

if __name__ == '__main__':
    main()
