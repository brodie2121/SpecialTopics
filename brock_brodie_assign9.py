class Employee:
    def __init__(self, Name, Id):
        self.Name = Name
        self.Id = Id


class ShiftSupervisor(Employee):
    def __init__(self, Name, Id, Salarie, Bonus):
        super().__init__(Name, Id)
        self.Salarie = Salarie
        self.Bonus = Bonus

    def display(self):
        print("Shift worker supervisor information:")
        print("Name:", self.Name)
        print("ID Number:", self.Id)
        print("Annual Salary:", self.Salarie)
        print("Annual Production Bonus:", self.Bonus)


Name = input("Enter the Name: ")
ID = input("Enter the ID: ")
Salarie = int(input("Enter the Annual Salary: "))
Bonus = int(input("Enter the Bonus: "))
shiftsupervisor1 = ShiftSupervisor(Name, ID, Salarie, Bonus)
shiftsupervisor1.display()
