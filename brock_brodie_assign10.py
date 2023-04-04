class Person:
    def __init__(self, fname, lname, email):
        self.firstName = fname
        self.lastName = lname
        self.email = email

    def getInformation(self):
        pass


class Customer(Person):
    def __init__(self, fname, lname, email, num):
        super().__init__(fname, lname, email)
        self.number = num


def getInformation(self):
    print("\nCustomer Information")
    print("Customer : ", self.firstName+' '+self.lastName)
    print("Customer Email : ", self.email)
    print("Customer Number : ", self.number, '\n')


class Employee(Person):
    def __init__(self, fname, lname, email, ssn):
        super().__init__(fname, lname, email)
        self.ssn = ssn


def getInformation(self):
    print("\nEmployee Information")
    print("Employee : ", self.firstName+' '+self.lastName)
    print("Employee Email : ", self.email)
    print("Employee Number : ", self.ssn, '\n')


def display(ob):
    if isinstance(ob, Customer):
        print("Customer Information")
    else:
        print("Employee Information")
    ob.getInformation()


while(True):
    fname = input("\nFirst name : ")
    lname = input("Last name : ")
    email = input("Email : ")
    choice = input("Customer or Employee ?(c/e) ")

    if choice == 'c':
        num = input("Number : ")
        c = Customer(fname, lname, email, num)
        c.getInformation()

    elif choice == 'e':
        ssn = input("SSN : ")
        e = Employee(fname, lname, email, ssn)
        e.getInformation()

    choice = input("Continue? (y/n) : ")

    if choice == 'n':
        break
print("Bye!")
